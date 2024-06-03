import cv2
import os
from time import sleep

def capture_photos(person_name, photos_per_person=100):
    # Crear una carpeta para guardar las fotos de la persona si no existe
    person_folder = f'captured_photos/{person_name}'
    if not os.path.exists(person_folder):
        os.makedirs(person_folder)

    # Iniciar la captura de video desde la cámara
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se puede acceder a la cámara.")
        return

    photo_count = 0
    max_digits = len(str(photos_per_person))
    while photo_count < photos_per_person:
        # Leer un frame de la cámara
        ret, frame = cap.read()
        
        if not ret:
            print("Error: No se puede leer el frame de la cámara.")
            break

        # Guardar la imagen con un nombre basado en el índice de la foto
        photo_filename = f'{person_folder}/photo_{str(photo_count + 1).zfill(max_digits)}.jpg'
        cv2.imwrite(photo_filename, frame)
        print(f'Foto guardada: {photo_filename}')
        photo_count += 1

        sleep(0.5)

    # Liberar la captura de video y cerrar todas las ventanas de OpenCV
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Nombre de la persona para la cual se van a capturar las fotos
    person_name = input("Ingrese el nombre de la persona: ")

    # Capturar al menos 100 fotos por persona
    capture_photos(person_name, photos_per_person=200)
