import io
import cv2
import numpy as np
from PIL import Image, ImageFilter

from .u2net import detect

model_u2net = detect.load_model(model_name="u2net")
model_u2netp = detect.load_model(model_name="u2netp")


def remove(data, model_name="u2net"):
    model = model_u2net

    if model == "u2netp":
        model = model_u2netp

    img = Image.open(io.BytesIO(data)).convert('RGB')
    roi = detect.predict(model, np.array(img))
    mask = roi.resize(img.size, resample=Image.LANCZOS).convert("L").filter(ImageFilter.MinFilter)
    empty = Image.new("RGBA", (img.size), 0)


    #old way    
    out = Image.composite(img, empty, mask)

    bio = io.BytesIO()
    out.save(bio, "PNG")

    return bio.getbuffer()
