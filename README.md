# 🤖 Instagram DM Bot (Flask + Meta Graph API)

This project is an automated Instagram Direct Message (DM) bot built using **Flask** and the **Meta Instagram Messaging API**.  
It receives messages via webhooks and sends automated replies based on simple logic.

---

## 🚀 Features

- 📩 Receives Instagram DMs via Webhooks
- 🤖 Automatically replies to user messages
- 🔁 Handles echo messages safely (prevents infinite loops)
- ✏️ Ignores message edits and system events
- 🔐 Uses environment variables for security
- ⚡ Lightweight Flask server

---

## 🧠 How It Works

1. Instagram sends a webhook event when a user sends a DM
2. Flask receives the event at `/webhook`
3. The bot extracts the message text
4. A response is generated using `get_response()`
5. The bot sends a reply using Meta Graph API

---

## 🛠️ Tech Stack

- Python 🐍
- Flask 🌐
- Meta Graph API (Instagram Messaging)
- Requests Library
- dotenv (.env management)

---

