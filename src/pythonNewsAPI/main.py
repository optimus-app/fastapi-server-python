# For FASTAPI and API requests
from typing import Optional
from fastapi import FastAPI
import requests
import httpx

# For os and environment variables for Langchain OpenAI and langchain agent
import os 
from dotenv import load_dotenv

# For Langchain
from langchain.agents import AgentType, initialize_agent
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_cohere import ChatCohere
from langchain_core.output_parsers import StrOutputParser

# Importing classes from the same package
from .polygon import StockRequestData;
from .langModel import StockRequestLangChain;

app = FastAPI()

# API for obtaining structured news data from polygon
# stockRequestData
#   - symbol: str  
#   - order: Optional[str] = "asc" (default)
#   - limit: Optional[str] = "5" (default)
@app.post("/stock-news-polygon")
async def stockNewsPolygon(request: StockRequestData):

    requestMsg = f"https://api.polygon.io/v2/reference/news?ticker={request.symbol}&order={request.order}&limit={request.limit}&apiKey=xj8EhRNHGdZW6BjW3DCH1Kw5Ie2_Ms4L"
    async with httpx.AsyncClient() as client:
        response = await client.get(requestMsg)
    return response.json()


# API for using langchain AI
# StockRequestLangChain
#   - symbol: str
#   - duration: Optional[str] = "today" (default)
@app.post("/stock-news-langchain")
async def stockNewsLangChain(request: StockRequestLangChain):

    # Obtain environment variables
    load_dotenv()
    cohereApiKey = os.getenv("COHERE_API_KEY") 

    tool = YahooFinanceNewsTool()
    llm = ChatCohere(cohere_api_key=cohereApiKey)
    output = StrOutputParser()

    chain = tool | llm | output
    result = chain.invoke(f"Tell me about the news about {request.symbol} for {request.duration}?")
    
    return {"result": str(result)}