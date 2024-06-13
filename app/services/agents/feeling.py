from PIL import Image
import numpy as np

import cv2
from mtcnn import MTCNN

import keras

model = keras.models.load_model('app\\agent_model\\model_fer.h5')

img_size = 160

def preprocess_new_image(img_array, img_shape=(img_size, img_size)):
    detector = MTCNN()
    img = img_array
    if img is not None:
        results = detector.detect_faces(img)
        if results:
            x1, y1, width, height = results[0]['box']
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
            face = img[y1:y2, x1:x2]
            face = cv2.resize(face, img_shape)
            face_gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            face_gray = np.expand_dims(face_gray, axis=-1)
            face_gray = face_gray / 255.0  # Normalizar la imagen
            return np.expand_dims(face_gray, axis=0)  # Agregar una dimensión para el batch
        else:
            print("No face detected in the image.")
            return None
    else:
        print("Error reading the image.")
        return None


categories = ['Angry', 'Neutral', 'Sad', 'Happy', 'Surprised']


def recognize_feeling_from_image(file_storage_image):
    img = Image.open(file_storage_image)
    img_array = np.array(img)

    try:
        print("PRE-PROCESSING IMAGE")
        predicted_image = preprocess_new_image(img_array)
        if predicted_image is not None:
            print("Predicting Emotion:")
            prediction = model.predict(predicted_image)
            predicted_class = np.argmax(prediction, axis=1)
            predicted_emotion = categories[predicted_class[0]]

            return {"prediction" :predicted_emotion}
        else:
            return "No face detected or error in preprocessing."
    except Exception as e:
        return f"Error processing image: {str(e)}"