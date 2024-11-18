from pydantic import BaseModel
from typing import Optional

class StockRequestData(BaseModel):
    
    symbol: str                         # Symbol of the Stock
    order: Optional[str] = "asc"        # Order: asc/desc
    limit: Optional[str] = "5"          # Limit: E.g. 10`