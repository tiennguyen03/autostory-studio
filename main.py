import requests
from openai import OpenAI
from supabase import create_client, Client
from core.tts_helper import generateVoiceOvers
from core.openai_helper import generateScript, generateBeats
from core.config import OPENAI_API_KEY, SUPABASE_KEY, SUPABASE_URL, ELEVENLABS_API_KEY

openai = OpenAI(api_key=OPENAI_API_KEY)
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

try:
    with open("articles/robert-fisher.txt", "r", encoding="utf-8") as f:
        article_text = f.read()
except FileNotFoundError:
    print("❌ Article file not found")
    article_text = ""

print("⏳ Generating script, please wait...")

script = generateScript(article_text,approx_length=60)

print("\n✅ Script generated:\n")
print(f"{script}\n")

beats = generateBeats(script)

for beat in beats:
    print(f"{beat}\n")

print("\n✅ Beats generated:\n")

generateVoiceOvers(script)

print("\n✅ Voiceover generated:\n")
