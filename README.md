# 🎬 AutoStory Studio

**AutoStory Studio** is an AI-powered storytelling pipeline that converts long-form articles into short-form, visually cinematic TikTok-style stories. It automatically generates scripts, voiceovers, and MidJourney image prompts — then detects and downloads the generated images from Discord into organized project folders.

---

## 🚀 Features

✅ **Article-to-Script Generation**
- Converts any input article into a 90-second, beat-by-beat narrative script using OpenAI’s GPT-5-Mini model.
- Automatically formats each beat for visual storytelling clarity.

✅ **Automatic Voiceover Creation**
- Uses ElevenLabs API to synthesize professional-quality narration for the generated script.

✅ **MidJourney Prompt Generation**
- Creates cinematic, style-consistent image prompts for each beat.
- Prompts follow a master “courtroom sketch” art direction for visual cohesion.

✅ **Discord Image Detection & Saving**
- Listens to a designated Discord channel for MidJourney’s image messages.
- Automatically downloads and saves generated images (both attachments and embeds) into the correct project folder.

✅ **Project Management**
- Every story is stored in a structured directory under `/projects/`
  ```
  projects/
    case1/
      audio/
      images/
      animations/
      scripts/
      script.txt
      beats.txt
      prompts.txt
  ```
- Keeps all generated assets organized by case or project.

---

## 🧩 Tech Stack

| Component | Technology |
|------------|-------------|
| Scripting & Prompts | OpenAI GPT-5-Mini |
| Voice Generation | ElevenLabs API |
| Image Generation | MidJourney (via Discord bot) |
| Database (optional) | Supabase |
| Backend | Python 3.11 |
| Discord Automation | discord.py, aiohttp |
| Project Structure | pathlib, dotenv |

---

## 🧠 Workflow Overview

1. **Input Article**
   - Place your source text in `articles/test_sample.txt`

2. **Run Main Pipeline**
   ```bash
   python3 main.py
   ```

3. **Steps Executed:**
   - Initializes a new project folder
   - Generates script → saves to `scripts/script.txt`
   - Splits beats → saves to `scripts/beats.txt`
   - Creates ElevenLabs voiceover → saves to `audio/voiceover.mp3`
   - Builds MidJourney image prompts → saves to `prompts.txt`
   - Launches Discord listener to auto-download generated images

4. **Manual Step (for now)**
   - Paste image prompts into your MidJourney Discord channel.
   - The bot will detect MidJourney’s response and automatically save results into `/images`.

---

## ⚙️ Environment Setup

Create a `.env` file in your project root and include:

```
OPENAI_API_KEY=your_openai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
DISCORD_TOKEN=your_discord_bot_token
DISCORD_CHANNEL_ID=your_channel_id
DISCORD_GUILD_ID=your_guild_id
MJ_COMMAND_ID=938956540159881230
MJ_COMMAND_VERSION=1237876415471554623
SESSION_ID=your_session_id
```

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🗂️ Folder Structure

```
autostory-studio/
│
├── articles/                 # Source articles
├── core/                     # Core logic modules
│   ├── openai_helper.py      # Script + beat generation
│   ├── tts_helper.py         # Voiceover synthesis
│   ├── midjourney_helper.py  # Image prompt creation
│   ├── discord_helper.py     # Discord listener/downloader
│   ├── project_manager.py    # Project folder setup
│   └── config.py             # Env key loading
│
├── projects/                 # Organized story projects
│   └── case1/
│       ├── audio/
│       ├── images/
│       ├── animations/
│       ├── scripts/
│       ├── script.txt
│       ├── beats.txt
│       └── prompts.txt
│
├── main.py                   # Primary pipeline runner
└── .env                      # API credentials
```

---

## 🔮 Next Steps

- [ ] Automatically rename downloaded images (`beat1.png`, `beat2.png`, etc.)
- [ ] Add GUI for managing projects and visualizing outputs
- [ ] Integrate OpenAI Vision for generating animation prompts from images
- [ ] Add Supabase project sync for cloud storage

---

## 💡 Inspiration

This project was inspired by the need to automate TikTok-style storytelling — combining AI-written scripts, AI-generated art, and natural voice synthesis into a fully modular workflow for true-crime or documentary-style content.
