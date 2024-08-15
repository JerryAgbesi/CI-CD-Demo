
from fastapi import FastAPI
from .routes.books import appRouter

app = FastAPI(title = "Books API")


@app.get("/healthcheck")
def home():
    return{"message":"Books API is live"}

app.include_router(appRouter,prefix="/api/v1")