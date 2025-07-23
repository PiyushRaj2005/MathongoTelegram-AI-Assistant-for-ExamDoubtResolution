from gtts import gTTS
import os

def generate_audio(text, filename="response.mp3"):
    try:
        tts = gTTS(text=text, lang='hi')  # 'hi' works for Hinglish too
        path = os.path.join("tts", filename)
        tts.save(path)
        return path
    except Exception as e:
        print("TTS generation failed:", e)
        return None
