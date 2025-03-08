# For FASTAPI and API requests
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
import requests
import yfinance as yf

# For os and environment variables for Langchain OpenAI and langchain agent
import os 
from dotenv import load_dotenv

# For Langchain
from langchain.agents import AgentType, initialize_agent
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_cohere import ChatCohere
from langchain_core.output_parsers import StrOutputParser

# For input and output models
from models import StockRequestData, StockRequestLangChain, StockEntry, StockResponse

# Obtain environment variables
load_dotenv()
cohereApiKey = os.getenv("COHERE_API_KEY")

# Setting up a FAST API application
app = FastAPI()

# Configure CORS
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Actual implementation of APIs
@app.post("/stock-news-polygon")
def stockNewsPolygon(request: StockRequestData):

    requestMsg = f"https://api.polygon.io/v2/reference/news?ticker={request.symbol}&order={request.order}&limit={request.limit}&apiKey=xj8EhRNHGdZW6BjW3DCH1Kw5Ie2_Ms4L"
    response = requests.get(requestMsg)
    return response.json()

@app.post("/stock-news-langchain")
def stockNewsLangChain(request: StockRequestLangChain):

    tool = YahooFinanceNewsTool()
    llm = ChatCohere(cohere_api_key=cohereApiKey)
    output = StrOutputParser()

    chain = tool | llm | output
    result = chain.invoke(f"Tell me about today's news about {request.symbol}?")
    
    return {"result": str(result)}

# Stock Price API
@app.get("/stock-price/{symbol}", response_model=StockResponse)
@app.get("/stock-price/{symbol}?period={period}", response_model=StockResponse)
def stockPrice(symbol: str, period: str = "1d"):
    try:
        ticker = yf.Ticker(symbol)
        period_list = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max", "all"]
        interval_map = {
            "1d": "1m",
            "5d": "15m",
            "1mo": "1h",
            "3mo": "1d",
            "6mo": "1d",
            "1y": "1d",
            "2y": "1d",
            "5y": "5d",
            "10y": "1mo",
            "ytd": "1wk",
            "max": "1mo",
            "all": "1d"
        }
        if period not in period_list:
            raise HTTPException(status_code=404, detail="Invalid period. Please use one of the following: " + ", ".join(period_list))
        
        interval = interval_map[period]
        period = "max" if period == "all" else period
        hist = ticker.history(period=period, interval=interval, auto_adjust=False, back_adjust=False, actions=False)

        if hist.empty:
            raise HTTPException(status_code=404, detail="No data found for the given symbol.")
        
        entries = []
        for index, row in hist.iterrows():
            entries.append(StockEntry(
                date=index.strftime('%Y-%m-%d %H:%M:%S'),
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                close=row['Close'],
                volume=row['Volume']
            ))
        return StockResponse(symbol=symbol.upper(), entries=entries)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))