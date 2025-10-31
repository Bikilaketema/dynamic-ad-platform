from fastapi import FastAPI
import uuid, os, shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
app = FastAPI(title="Video Ad Generator API")

os.makedirs("static/uploads", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

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


@app.post("/api/v1/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    A generic endpoint that saves ANY file to 'static/uploads'
    and returns its new public URL.
    """
    
    file_extension = os.path.splitext(file.filename)[1]
    
    unique_filename = f"{uuid.uuid4()}{file_extension}"
    file_path = os.path.join("static/uploads", unique_filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
            
    return {
        "url": f"/static/uploads/{unique_filename}" 
    }