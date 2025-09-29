import requests
from openai import OpenAI
from supabase import create_client, Client
from core.midjourney_helper import makeImagePrompts
from core.project_manager import init_project
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

# Step 1 : Initialize Project 
print("⏳ Creating Project Directory, please wait...\n")
project_path = init_project("case1")

# Step 2 : Generate Script
print("⏳ Generating script, please wait...\n")
script = generateScript(article_text,approx_length=90)
print("\n✅ Script generated:\n")
print(f"{script}\n")

# Step 3 : Save Script to Script.txt
script_file = project_path / "script.txt"
script_file.write_text(script, encoding="utf-8")
print(f"💾 Script saved to {script_file}")

# Step 4 : Break script into beats
print("⏳ Generating beats, please wait...\n")
beats = generateBeats(script)
print("\n✅ Beats generated:\n")

for i, beat in enumerate(beats, start=1):
    print(f"Beat {i}: {beat}\n")

# Step 5 : Saving Beats to beats.txt
beats_text = "\n".join(beats) # Joins beats into one stringe seperates by "\n"
beats_file = project_path / "beats.txt"
beats_file.write_text(beats_text, encoding="utf-8")
print(f"💾 Beats saved to {beats_file}")

# Step 6: Generate Voiceover
audio_file = project_path / "audio" / "voiceover.mp3"
print("⏳ Generating voiceover, please wait...\n")
generateVoiceOvers(script,audio_file)


# Step 7: Generate Image Generation Prompts
print("⏳ Generating image generation prompts, please wait...\n")
images_file = project_path / "prompts.txt"
image_prompts = makeImagePrompts(beats,master_style_prompt,article_text)
images_text = "\n\n".join(image_prompts)
images_file.write_text(images_text, encoding="utf-8")


print("\n✅ Image prompts generated:\n")

for i, prompt in enumerate(image_prompts, start=1):
    print(f"Prompt {i}: {prompt}\n")

