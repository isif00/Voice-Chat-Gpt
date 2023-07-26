from gtts import gTTS
import os

language = 'en'

def text_to_speech(text):
    myobj = gTTS(text=text, lang=language, slow=False)
  
    # Saving the converted audio in a mp3 file named
    myobj.save("answer.mp3")
    
    # Playing the converted file
    os.system("answer.mp3")