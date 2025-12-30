from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="Aegis Code Analyzer",
    description="Microservice for AST parsing and Static Analysis",
    version="1.0.0"
)

# Register the routes
app.include_router(router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    # Hot-reload enabled for development
    uvicorn.run("src.main:app", host="127.0.0.1", port=8001, reload=True)