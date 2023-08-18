from fastapi import FastAPI
from src.apis.extraction_api import router as ExtractionApiRouter


app = FastAPI(title="Web Scraping project")
app.include_router(ExtractionApiRouter)