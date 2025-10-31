from fastapi import FastAPI

app = FastAPI(title="Video Ad Generator API")

@app.get("/")
async def get_root():
    """
    This is the root endpoint. It's a simple health check.
    """
    return {"message": "Welcome to the Ministry Ad Generator API!"}


@app.get("/api/v1/status")
async def get_status():
    """
    Returns the current status of the API.
    """
    return {"status": "running", "message": "Ready to generate ads!"}