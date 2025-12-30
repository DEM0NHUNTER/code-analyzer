from fastapi import APIRouter, HTTPException
from src.api.models import AnalysisRequest, AnalysisResponse
from src.analyzer.core import CodeAnalyzer

router = APIRouter()


@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_code(payload: AnalysisRequest):
    """
    Accepts Python code, analyzes it, and returns complexity metrics.
    """

    # 1. Call the Core Logic
    # Note: In a real heavy CPU task, we would use 'run_in_threadpool' here
    # but for this demo, direct calling is fine.
    metrics = CodeAnalyzer.analyze_snippet(payload.code_snippet)

    # 2. Calculate aggregates (Business Logic)
    total_functions = len(metrics)

    if total_functions > 0:
        avg_complexity = sum(m.complexity for m in metrics) / total_functions
    else:
        avg_complexity = 0.0

    # 3. Return structured JSON
    return AnalysisResponse(
        filename="snippet.py",
        total_functions=total_functions,
        metrics=metrics,
        average_complexity=round(avg_complexity, 2)
    )


@router.get("/health")
async def health_check():
    return {"status": "ok", "service": "code-analyzer"}