from fastapi import FastAPI
from core.config import settings

app = FastAPI(title=settings.PROJECT_TITLE, version=settings.PROJECT_VERSION, summary= settings.PROJECT_SUMMARY)

@app.get("/")
def hello():
    return "Tonight's special: 🍲 Chicken Curry!\nBreakfast is served! 🍳🥓🥞"