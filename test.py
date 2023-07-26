import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import scipy.io.wavfile as wav

r = sr.Recognizer()

def convert_audio_to_text(file_name):
    # open the file
    with sr.AudioFile(file_name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        prompt = r.recognize_google(audio_data)
        return prompt

convert_audio_to_text("sample.wav")