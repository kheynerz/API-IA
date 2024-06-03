import cv2
import time
import os
import argparse

emotions = ["happy", "sad", "angry", "surprised", "neutral"]

def capture_photos(photo_count, sleep_time, emotion):
    emotion_folder = f'captured_photos/{emotion}'
    if not os.path.exists(emotion_folder):
        os.makedirs(emotion_folder)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se puede acceder a la cámara.")
        return

    for i in range(photo_count):
        ret, frame = cap.read()
        
        if not ret:
            print("Error: No se puede leer el frame de la cámara.")
            break

        photo_filename = f'{emotion_folder}/photo_{i}.jpg'
        cv2.imwrite(photo_filename, frame)
        print(f'Foto guardada: {photo_filename}')

        time.sleep(sleep_time)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Capturar fotos desde la cámara cada segundo para diferentes emociones.")
    parser.add_argument("-c", type=int, nargs='?', default=20, help="Número de fotos a capturar por emoción (por defecto 10)")
    parser.add_argument("-s", type=int, nargs='?', default=1, help="Intervalo en segundos para la captura de las fotos (por defecto 1)")
    
    args = parser.parse_args()

    photo_count = args.photo_count
    sleep_time = args.sleep_time

    for emotion in emotions:
        print(f"Se capturarán {photo_count} fotos para la emoción: {emotion}")
        input("Presiona cualquier tecla para empezar...")
        capture_photos(photo_count, sleep_time, emotion)
        print(f"Fotos para la emoción {emotion} completadas.\n")

