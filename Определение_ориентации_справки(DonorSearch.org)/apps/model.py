from torchvision import transforms
from PIL import Image
import torch
import torch.nn as nn
from torchvision.models import resnet18,ResNet18_Weights
import numpy as np
transform = transforms.Compose([  # Изменение размера изображения
    transforms.ToTensor(),
    transforms.Resize((224, 224)),# преобразует изображение в тензор и нормализует пиксели в диапазон [0, 1]
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # нормализует значения по каналам
])

def load_model(model_path: str):
    model = torch.load(model_path)
    model.eval()
    return model
def predict_image(model, image: Image.Image):
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output,1)
    return predicted.item()