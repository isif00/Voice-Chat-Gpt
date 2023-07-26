import speech_recognition as sr
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
import scipy.io.wavfile as wav


# initialize the recognizer
r = sr.Recognizer()

# Sampling frequency
freq = 44100

# Recording duration
duration = int(input("how many seconds do u want to talk: "))

def record_audio(file_name):
    # Start recorder with the given values of 
    # duration and sample frequency
    recording = sd.rec(duration * freq, samplerate=freq, channels=2)

    # Record audio for the given number of seconds
    sd.wait()

    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    wav.write(file_name, freq, recording)

def convert_audio_to_text(file_name):
    print("starting ...")
    # open the file
    with sr.AudioFile(file_name) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        prompt = r.recognize_google(audio_data)
        return prompt

    