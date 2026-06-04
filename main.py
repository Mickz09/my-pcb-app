from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from PIL import Image
import io

# Import RTDETR 
from ultralytics import RTDETR 

app = FastAPI(title="PCB Solder Defect API")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load newly trained RT-DETR model
model = RTDETR("best.pt") 

@app.get("/")
async def serve_index():
    return FileResponse("static/index.html")

@app.post("/api/analyze")
async def analyze_image(file: UploadFile = File(...)):
    # Read the uploaded image
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes))

    # Run the AI inference (The rest of this function stays exactly the same!)
    results = model(image)
    
    defects_list = []
    
    for i, box in enumerate(results[0].boxes):
        x, y, w, h = box.xywhn[0].tolist()
        conf = float(box.conf[0]) * 100
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        
        defects_list.append({
            "id": i + 1,
            "type": class_name,
            "x": x * 100,
            "y": y * 100,
            "width": w * 100,
            "height": h * 100
        })
        
    avg_conf = sum(d["confidence"] for d in defects_list) / len(defects_list) if defects_list else 100
    
    final_response = {
        "prediction": "Defective" if len(defects_list) > 0 else "Good",
        "defect": f"Found {len(defects_list)} defect(s)" if defects_list else "No defects detected",
        "confidence": round(avg_conf, 1),
        "recommendation": "Inspect highlighted areas." if defects_list else "Pass to next station.",
        "defects": defects_list
    }

    return final_response

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
