from pydantic import BaseModel, Field
from typing import List, Optional


# REQUEST: What we accept from the user
class AnalysisRequest(BaseModel):
    code_snippet: str = Field(
        ...,
        description="The raw Python source code to analyze",
        min_length=10,
        example="def hello():\n    print('Hello world')"
    )


# RESPONSE: What we return
class FunctionMetric(BaseModel):
    name: str
    complexity: int
    line_number: int
    is_complex: bool  # Simple flag: True if complexity > 10


class AnalysisResponse(BaseModel):
    filename: str = "snippet.py"
    total_functions: int
    metrics: List[FunctionMetric]
    average_complexity: float
