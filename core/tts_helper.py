import os
import requests
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

if not ELEVENLABS_API_KEY:
    raise EnvironmentError("Missing ELEVENLABS_API_KEY in environment variables.")

eleven = ElevenLabs(api_key=ELEVENLABS_API_KEY)

def generateVoiceOvers(script_text, 
                       output_file="voiceover.mp3",
                       voice_id="MFZUKuGQUsGJPQjTS4wC", 
                       voice_settings=None):

    elevenLabsURL = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type" : "application/json"
    }

    # Default settings if none provided
    if voice_settings is None:
        voice_settings = {
            "speed": 0.9,
            "stability": 0.5,
            "similarity_boost": 0.75,
            "style_exaggeration": 0.0
        }

    data = {
        "text": script_text,
        "voice_settings": voice_settings
    }

    resp = requests.post(elevenLabsURL, headers=headers, json=data)

    if resp.status_code == 200:
        with open("voice_test.mp3","wb") as f:
            f.write(resp.content)
        print("Voiceover saved to {output_file}")
    else: print(f"Error {resp.status_code}: {resp.text}")