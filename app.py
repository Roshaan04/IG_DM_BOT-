
from flask import Flask, request
from dotenv import load_dotenv
import requests
import os
from responses import get_response

# -----------------------------------
# LOAD ENVIRONMENT VARIABLES
# -----------------------------------
load_dotenv()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

print("\n==============================")
print("BOT STARTING")
print("PAGE_ID:", PAGE_ID)
print("VERIFY_TOKEN:", VERIFY_TOKEN)
print("ACCESS TOKEN FOUND:", bool(ACCESS_TOKEN))
print("==============================\n")

app = Flask(__name__)

# -----------------------------------
# WEBHOOK VERIFICATION
# -----------------------------------
@app.route("/webhook", methods=["GET"])
def verify_webhook():

    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    print("\n🔵 VERIFY REQUEST RECEIVED")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("✅ WEBHOOK VERIFIED")
        return challenge, 200

    print("❌ WEBHOOK VERIFICATION FAILED")
    return "Verification failed", 403


# -----------------------------------
# WEBHOOK EVENTS
# -----------------------------------
@app.route("/webhook", methods=["POST"])
def webhook():

    data = request.get_json()

    print("\n🔥 POST RECEIVED")
    print("RAW DATA:", data)

    if not data:
        return "NO DATA", 200

    if data.get("object") != "instagram":
        print("⚠️ Not Instagram")
        return "IGNORED", 200

    for entry in data.get("entry", []):

        for event in entry.get("messaging", []):

            sender_id = event.get("sender", {}).get("id")
            recipient_id = event.get("recipient", {}).get("id")

            print("\n----------------------------")
            print("SENDER:", sender_id)
            print("RECIPIENT:", recipient_id)

            # Ignore edits
            if "message_edit" in event:
                print("✏️ Message Edit Ignored")
                continue

            # Ignore reads
            if "read" in event:
                print("👀 Read Event Ignored")
                continue

            # Ignore deliveries
            if "delivery" in event:
                print("📦 Delivery Event Ignored")
                continue

            message = event.get("message", {})

            # Ignore bot echoes
            if message.get("is_echo"):
                print("🔁 Echo Ignored")
                continue

            text = message.get("text")

            print("MESSAGE:", text)

            if not text:
                print("⚠️ No text found")
                continue

            print(f"📩 USER SAID: {text}")

            try:

                reply = get_response(text)

                print(f"🤖 BOT REPLY: {reply}")

                send_message(sender_id, reply)

            except Exception as e:
                print("❌ BOT ERROR:", str(e))

    return "EVENT_RECEIVED", 200


# -----------------------------------
# SEND MESSAGE
# -----------------------------------
def send_message(recipient_id, text):

    url = f"https://graph.facebook.com/v19.0/{PAGE_ID}/messages"

    payload = {
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": text
        },
        "messaging_type": "RESPONSE"
    }

    params = {
        "access_token": ACCESS_TOKEN
    }

    print("\n📤 SENDING MESSAGE")
    print("PAGE ID:", PAGE_ID)
    print("RECIPIENT:", recipient_id)
    print("TEXT:", text)

    try:

        response = requests.post(
            url,
            json=payload,
            params=params
        )

        print("STATUS:", response.status_code)

        try:
            print("JSON RESPONSE:", response.json())
        except:
            print("RAW RESPONSE:", response.text)

    except Exception as e:
        print("❌ SEND ERROR:", str(e))


# -----------------------------------
# HEALTH CHECK
# -----------------------------------
@app.route("/", methods=["GET"])
def home():
    return "Instagram Bot Running", 200


# -----------------------------------
# RUN APP
# -----------------------------------
if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
