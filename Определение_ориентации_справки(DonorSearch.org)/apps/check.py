import cv2
from PIL import Image
import numpy as np
def check_degree(image: Image.Image, result: int):
    image = np.array(image)
    h, w = image.shape[:2]
    center = (h // 2, w // 2)
    checker = {
        0: 0,
        1: 90,
        2: 180,
        3: 270
    }
    m = cv2.getRotationMatrix2D(center, angle = checker[result], scale = 1)
    rotated_image = cv2.warpAffine(image, m, (w, h))
    final_image = Image.fromarray(rotated_image)
    return final_image 
