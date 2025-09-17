import requests
from openai import OpenAI
from supabase import create_client, Client
from core.midjourney_helper import makeImagePrompts
from core.tts_helper import generateVoiceOvers
from core.openai_helper import generateScript, generateBeats
from core.config import OPENAI_API_KEY, SUPABASE_KEY, SUPABASE_URL, ELEVENLABS_API_KEY

openai = OpenAI(api_key=OPENAI_API_KEY)
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

master_style_prompt = """
Expressive painterly courtroom sketch style illustration, heavy black brushstrokes mixed with pencil shading, rough textured paper look, strong bold lines with visible paint strokes. Full color rendering with muted but rich tones (deep reds, ochres, blues, greens) layered like oil pastels, applied roughly with brush texture. Faceless characters or minimal obscured facial detail, features hidden in shadow. Semi-stylized, gritty, unsettling tone. Harsh lighting with deep shadows, cinematic dramatic framing. Style resembles reportage illustration mixed with oil pastel and charcoal, raw and emotional. --v 7 --ar 9:16 --q 2 --stylize 500 --chaos 15 --style raw
"""

try:
    with open("articles/test_sample.txt", "r", encoding="utf-8") as f:
        article_text = f.read()
except FileNotFoundError:
    print("❌ Article file not found")
    article_text = ""

print("⏳ Generating script, please wait...")

script = generateScript(article_text,approx_length=90)

print("\n✅ Script generated:\n")
print(f"{script}\n")

print("⏳ Generating beats, please wait...")

beats = generateBeats(script)

print("\n✅ Beats generated:\n")

for i, beat in enumerate(beats, start=1):
    print(f"Beat {i}: {beat}\n")

print("⏳ Generating voiceover, please wait...")

generateVoiceOvers(script)

print("\n✅ Voiceover generated:\n")

print("⏳ Generating image generation prompts, please wait...")

image_prompts = makeImagePrompts(beats,master_style_prompt,article_text)

print("\n✅ Image prompts generated:\n")

for i, prompt in enumerate(image_prompts, start=1):
    print(f"Prompt {i}: {prompt}\n")

