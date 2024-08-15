from fastapi import FastAPI
app = FastAPI(title = "Books API")


@app.get("/healthcheck")
def home():
    return{"message":"Books API is live"}

