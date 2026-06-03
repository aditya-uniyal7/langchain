from pydantic import BaseModel, Field

class Debug(BaseModel):
    bugtype: str = Field(description="Description of the bug type (e.g., Syntax, Logic)")
    exp: str = Field(description="Details of the reason why the bug occurred")
    fixed: str = Field(description="The fully corrected and working code snippet")