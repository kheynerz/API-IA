from deepface import DeepFace as df
from PIL import Image
import numpy as np

def recognize_feeling_from_image(file_storage_image):
    img = Image.open(file_storage_image)
    img_array = np.array(img)

    try:
        face_analysis = df.analyze(img_array,  actions = ['emotion'], silent=True)
    except:
        raise Exception("Error processing image")
    
    return face_analysis