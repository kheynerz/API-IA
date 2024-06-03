import cv2
import time
import os
import sys

emotions = ["happy", "sad", "angry", "surprised", "neutral"]

def capture_photos(total_photo_count, sleep_time, emotion, initialIndex):
    emotion_folder = f'captured_photos/{emotion}'
    if not os.path.exists(emotion_folder):
        os.makedirs(emotion_folder)

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se puede acceder a la cámara.")
        return

    max_digits = 3

    for i in range(initialIndex * total_photo_count, initialIndex * total_photo_count + total_photo_count):
        ret, frame = cap.read()
        
        if not ret:
            print("Error: No se puede leer el frame de la cámara.")
            break
        photo_filename = f'{emotion_folder}/{str(i + 1).zfill(max_digits)}.jpg'
        cv2.imwrite(photo_filename, frame)
        print(f'Foto guardada: {photo_filename}')

        time.sleep(sleep_time)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    total_photo_count = 20
    sleep_time = 1

    if len(sys.argv) > 1:
        initialIndex = int(sys.argv[1])
    else:
        initialIndex = 0
    for emotion in emotions:
        print(f"Se capturarán un total de {total_photo_count} fotos para la emoción: {emotion}")
        input('Presiona "Enter"  para empezar...')
        capture_photos(total_photo_count, sleep_time, emotion, initialIndex)
        print(f"Fotos para la emoción {emotion} completadas.\n")

