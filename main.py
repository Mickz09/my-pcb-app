from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import io
import random
from PIL import Image

# Import your vision model framework here
# from ultralytics import YOLO, RTDETR

app = FastAPI(title="PCB Solder Defect API")

# Mount the static directory so the frontend can be served
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize your computer vision model
# model = RTDETR('best.pt') 

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

@app.post("/api/analyze")
async def analyze_image(file: UploadFile = File(...)):
    # 1. Read the uploaded image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # 2. Run inference
    # results = model(image)
    
    # 3. Process your model's bounding boxes and classes into this dictionary format
    # Below is a mock response matching your React state requirements
    mock_responses = [
        {
            "prediction": "Defective",
            "defect": "Solder Bridge",
            "confidence": 92,
            "recommendation": "Remove excess solder and reinspect nearby pins.",
            "defects": [
                {"id": 1, "type": "Solder Bridge", "x": 48, "y": 42, "size": 96}
            ]
        },
        {
            "prediction": "Good",
            "defect": "No Defect",
            "confidence": 96,
            "recommendation": "The solder joint passed visual classification.",
            "defects": []
        }
    ]

    return random.choice(mock_responses)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)