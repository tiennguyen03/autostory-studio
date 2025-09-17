# chatgpt_helper.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise EnvironmentError("❌ Missing OPENAI_API_KEY in environment variables.")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

def makeImagePrompts(beats,style,article_text=""):

    if not beats or not isinstance(beats, list):
        raise ValueError("Beats must be a non-empty list of strings.")
    
    image_prompts = []
    
    for i, beat in enumerate(beats, start=1):
        user_prompt = (
            f"You are helping create MidJourney image prompts for a true-crime TikTok video.\n\n"
            f"Beat {i}: {beat}\n\n"
            f"Source article (for accuracy): {article_text[:1000]}...\n\n"  # trim if very long
            f"Task: Rewrite this beat as a **visual scene description** for an AI image generator.\n"            
            f"Style: {style}\n\n"
            f"Important:\n"
            f"- Do not repeat the beat word-for-word.\n"
            f"- Keep the scene factual to the case.\n"
            f"- Describe setting, people, and atmosphere visually.\n"
            f"- Use concise, cinematic phrasing.\n"
            f"- End with MidJourney params: --ar 16:9 --v 5\n"
        )

        resp = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that generates cinematic MidJourney prompts."},
                {"role": "user", "content": user_prompt}
            ]
        )
    
        if not resp.choices or not resp.choices[0].message:
            raise RuntimeError(f"❌ No response for beat {i}")

        image_prompt = resp.choices[0].message.content.strip()
        image_prompts.append(image_prompt)
    return image_prompts


