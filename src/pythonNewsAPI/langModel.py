from pydantic import BaseModel
from typing import Optional

class StockRequestLangChain(BaseModel):
    symbol: str                         # Symbol of the Stock
    duration: Optional[str] = "today"     # How latest the data do you want