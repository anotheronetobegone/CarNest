from fastapi import FastAPI

app = FastAPI(
    title="CarNest API",
    version="1.0.0"
)

@app.get("/")
def home():
    """
    Initial endpoint
    """

    return {
        "message": "Welcome to CarNest API"
    }