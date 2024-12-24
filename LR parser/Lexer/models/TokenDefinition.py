from pydantic import BaseModel


class TokenDefinition(BaseModel):
    name: str
    pattern: str
    
