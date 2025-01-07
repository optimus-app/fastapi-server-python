from typing import Optional, List
from pydantic import BaseModel

# Inputs for two APIs
class StockRequestData(BaseModel):
    symbol: str                         # Symbol of the Stock
    order: Optional[str] = "asc"        # Order: asc/desc
    limit: Optional[str] = "5"          # Limit: E.g. 10

class StockRequestLangChain(BaseModel):
    symbol: str                         # Symbol of the Stock

# Outputs for Stock Data API
class StockEntry(BaseModel):
    date: str
    open: float
    high: float
    low: float
    close: float
    volume: int

class StockResponse(BaseModel):
    symbol: str
    entries: List[StockEntry]