# 🤖 Instagram DM Bot (Flask + Meta Graph API)

This project is an automated Instagram Direct Message (DM) bot built using **Flask** and the **Meta Instagram Messaging API**.  
It receives messages via webhooks and sends automated replies based on simple logic.

---

## ⚡ Features

- 🤖 Auto-reply Instagram DM bot  
- 🧠 Keyword-based message understanding  
- 🍔 Menu & food inquiry responses  
- 💰 Pricing and payment support  
- 🚚 Delivery information handling  
- 📅 Table reservation automation  
- ⏰ Opening/closing time responses  
- 🎁 Offers and discount messages  
- 🔗 Meta Webhook integration  
- 🔐 Secure environment variable setup  
- 🧪 Local testing using ngrok  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|--------|
| Python 3.8+ | Backend logic |
| Flask | Web server & API handling |
| Requests | HTTP API calls |
| python-dotenv | Environment variables |
| Meta Graph API v18 | Instagram messaging |
| ngrok | Local webhook testing |

---

## 🏗️ Architecture

1. User sends Instagram DM  
2. Meta Webhook forwards message to Flask server  
3. Flask extracts message & sender ID  
4. Keyword engine detects intent  
5. Response generated automatically  
6. Reply sent back via Graph API  

---

## 📦 Installation

### Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/eat-and-greet-bot.git
cd eat-and-greet-bot
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create `.env` File
```env
ACCESS_TOKEN=your_access_token_here
VERIFY_TOKEN=your_verify_token_here
PORT=5000
```

---

## ⚙️ Meta Configuration

### 1. Create Meta App
- Go to developers.facebook.com  
- Create a Business App  
- Add Instagram Graph API + Messenger  

---

### 2. Required Permissions
```
pages_manage_metadata
pages_messaging
instagram_basic
instagram_manage_messages
pages_read_engagement
```

---

### 3. Webhook Setup

Start ngrok:
```bash
ngrok http 5000
```

Example webhook URL:
```
https://your-ngrok-url.ngrok-free.app/webhook
```

- Paste into Meta Webhook settings  
- Set Verify Token same as `.env`  
- Subscribe to `messages` event  

---

## 🚀 Run Project

### Start Flask Server
```bash
python app.py
```

### Start ngrok (new terminal)
```bash
ngrok http 5000
```

---

## 🧪 Testing

| Message | Expected Response |
|--------|------------------|
| hi | Welcome message |
| menu | Food categories |
| price | Pricing details |
| delivery | Delivery info |
| book table | Reservation flow |
| timing | Opening hours |
| payment | Payment methods |
| deal | Offers & discounts |

---

## 📁 Project Structure

```
Eat-and-Greet-Bot/
│
├── app.py
├── responses.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🔁 Response Logic

- Greetings → Welcome message  
- Menu → Food list  
- Price → Pricing details  
- Delivery → Delivery info  
- Bookings → Reservation flow  
- Payment → Payment methods  
- Deals → Discounts/offers  

---

## 🌍 Deployment

### Render
- Connect GitHub repo  
- Add environment variables  
- Deploy service  

### Railway
- Import project  
- Add `.env` variables  
- Deploy instantly  

---

## 🧯 Common Issues

**Webhook not verifying**
- Check ngrok URL  
- Verify token must match `.env`

**No response from bot**
- Ensure `messages` subscription is enabled  
- Check access token permissions  

**Ngrok link changes**
- Free version changes URL each restart  

---

## 🚀 Future Improvements

- AI-powered responses (LLM integration)  
- Database for chat history  
- Multi-language support  
- Analytics dashboard  
- Image/menu cards  
- Memory-based conversations  

---

## 👨‍💻 Author

**Roshaan Jadoon**  
AI Automation Intern — Codecelix  

---

