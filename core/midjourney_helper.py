# chatgpt_helper.py
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from the .env file into environment variables.
# This allows you to keep sensitive keys (like API keys) outside your codebase.
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Ensure the API key is set; otherwise, stop execution early with an error.
if not api_key:
    raise EnvironmentError("❌ Missing OPENAI_API_KEY in environment variables.")

# Initialize the OpenAI client with the loaded API key.
client = OpenAI(api_key=api_key)

def makeImagePrompts(beats, style, article_text=""):
    """
    Takes an array of 'beats' (short narrative segments) and generates
    cinematic MidJourney image prompts for each beat.

    Args:
        beats (list[str]): A list of narration beats from the script.
        style (str): A master style prompt to ensure visual consistency.
        article_text (str): Optional source text for accuracy/context.

    Returns:
        list[str]: A list of AI-generated MidJourney prompts, one per beat.
    """

    # Validate input to avoid empty or incorrect types.
    if not beats or not isinstance(beats, list):
        raise ValueError("Beats must be a non-empty list of strings.")
    
    image_prompts = []  # will collect all generated prompts
    
    # Loop through each beat and generate an image prompt
    for i, beat in enumerate(beats, start=1):
        # Construct a user prompt for the OpenAI model
        # It instructs ChatGPT to rewrite the narration beat into
        # a visual description suitable for image generation.
        user_prompt = (
            f"You are helping create MidJourney image prompts for a true-crime TikTok video.\n\n"
            f"Beat {i}: {beat}\n\n"
            f"Source article (for accuracy): {article_text[:1000]}...\n\n"  # trim article text to avoid sending too much
            f"Task: Rewrite this beat as a **visual scene description** for an AI image generator.\n"            
            f"Style: {style}\n\n"
            f"Important:\n"
            f"- Do not repeat the beat word-for-word.\n"
            f"- Keep the scene factual to the case.\n"
            f"- Describe setting, people, and atmosphere visually.\n"
            f"- Use concise, cinematic phrasing.\n"
            f"- End with MidJourney params: --v 7 --ar 9:16 --q 2 --style raw --chaos 12\n"
        )

        # Call the OpenAI chat completion API
        resp = client.chat.completions.create(
            model="gpt-5-mini",  # small, cheaper model used for prompt generation
            messages=[
                {"role": "system", "content": "You are an assistant that generates cinematic MidJourney prompts."},
                {"role": "user", "content": user_prompt}
            ]
        )
    
        # Error handling: ensure we got a valid response
        if not resp.choices or not resp.choices[0].message:
            raise RuntimeError(f"❌ No response for beat {i}")

        # Extract and clean up the generated prompt text
        image_prompt = resp.choices[0].message.content.strip()

        # Add it to the list of prompts
        image_prompts.append(image_prompt)

    # Return all generated prompts as a list
    return image_prompts