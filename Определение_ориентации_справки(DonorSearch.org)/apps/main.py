from fastapi import FastAPI,UploadFile,File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from PIL import Image
import io
from apps.model import load_model,predict_image
import numpy as np
from fastapi.responses import StreamingResponse
from apps.check import check_degree


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
model = load_model('apps/resnet18.pth')
@app.post('/predict/')
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    prediction = predict_image(model ,image)
    rotated_image = check_degree(image, prediction)
    buf = io.BytesIO()
    rotated_image.save(buf, format="JPEG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/jpeg")
