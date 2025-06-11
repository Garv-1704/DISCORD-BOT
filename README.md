# DISCORD-BOT
Discord bot that automates tasks and enhances user interaction within a server. It can respond to commands, deliver custom messages, and perform useful functions like moderation, reminders, or fetching data from APIs. Built using Python and the discord.py library
# MemeBot 🤖 - A Fun Discord Bot with Memes, Greetings, and Reactions

MemeBot is a lightweight and fun Discord bot written in Python using the `discord.py` library. It can greet users, reply to common phrases, and even fetch random memes from Reddit using the Meme API.

---

## 🚀 Features

- 🤖 Responds to "hello" and "how are you?"
- 😂 Fetches random memes from Reddit using [Meme API](https://github.com/D3vd/Meme_Api)
- 💬 Reacts to messages with emojis
- 🔧 Easy to set up and run

---

## 📦 Requirements

Before you get started, make sure you have:

- Python 3 installed
- `pip` (Python package installer)
- A Discord account
- A Discord server where you have "Manage Server" permissions

---

## ⚙️ Setup: Discord Developer Portal

### 1. Go to Developer Portal
Visit [https://discord.com/developers/applications](https://discord.com/developers/applications) and log in.

### 2. Create a New Application
- Click **New Application**.
- Name your application (e.g., `MemeBot`).

### 3. Add a Bot to Your Application
- In the left panel, click **Bot**.
- Click **Add Bot**.

### 4. Get Your Bot Token
> ⚠️ Treat this like a password! Never share or upload it publicly.

- Click **Reset Token**.
- Copy and save the token securely.

### 5. Invite Your Bot to a Server
- Under **OAuth2 → URL Generator**:
  - Select `bot` under **Scopes**.
  - Under **Bot Permissions**, select:
    - `Send Messages`
    - `Add Reactions`
    - `Read Message History`
- Copy the generated URL and open it in your browser to invite the bot.

---

## 🛠️ Install Dependencies
### For macOS/Linux:
python3 -m pip install -U discord.py
## If you are using Windows, then the following command should be used instead:
py -3 -m pip install -U discord.py
Create a file named bot.py and add your bot code (or use the one provided in this repo).
Make sure it includes:
discord.py for bot interaction
requests and json to fetch memes from the Meme API
Example API for memes:
https://meme-api.com/gimme
Run the Bot
bash
Copy
Edit
python3 bot.py
(Use py bot.py on Windows)
To stop the bot, press CTRL+C
🤖 Sample Commands
Try these in your Discord server after the bot is running:
hello → Bot says hello back
how are you → Friendly response
!meme → Fetches a random meme
Bot may react to messages with emojis for fun!

🧠 About
This bot is a great starter project to explore Discord bot development using Python. It combines text handling, third-party APIs, and emoji reactions in a fun and interactive way.

💡 Credits
discord.py

Meme API by D3vd

