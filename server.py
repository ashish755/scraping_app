from fastapi import FastAPI
from src.apis.extraction_api import router as ExtractionApiRouter


app = FastAPI(title="Data extraction project")
app.include_router(ExtractionApiRouter)
