
from fastapi import FastAPI
from contextlib import asynccontextmanager


from .routes.books import appRouter
from .db.database import Base,engine


@asynccontextmanager
async def db_init(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title = "Books API",lifespan=db_init)


@app.get("/")
def home():
    return{"message":"Books API is live, navigate to /docs to start using it"}

app.include_router(appRouter,prefix="/api/v1")