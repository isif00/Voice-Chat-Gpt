import os
import openai
from dotenv import load_dotenv
from VoiceToText import record_audio, convert_audio_to_text
from TextToVoice import text_to_speech

load_dotenv()
openai.api_key = os.getenv("SECTERT_KEY")

file_name = "sample.wav"
record_audio(file_name)
prompt = convert_audio_to_text(file_name)

def chat_with_chatgpt(prompt, model="gpt-3.5-turbo"):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message

text_result = chat_with_chatgpt(prompt)

text_to_speech(text_result)
