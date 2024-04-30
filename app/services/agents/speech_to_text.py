from io import BytesIO
import speech_recognition as sr

import pydub

def convert_to_wav(input_file):
    sound = pydub.AudioSegment.from_file(input_file)
    sound = sound.set_frame_rate(44100).set_channels(1)
    return sound

def speech_recognition(audio):
    recognizer = sr.Recognizer()
    audio_wav = convert_to_wav(audio)

    wav_file = audio_wav.export(format="wav")

    with sr.AudioFile(wav_file) as file:
        audio_data = recognizer.record(file)
        try:
            text = recognizer.recognize_google(audio_data, language='es-ES')
            return {"speech_to_text": text}, 200
        except sr.UnknownValueError:
            return {"error": "No se pudo reconocer el audio"}, 400
        except sr.RequestError as e:
            return {"error": f"No se pudo completar la solicitud: {e}"}, 500