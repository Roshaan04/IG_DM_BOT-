def get_response(text):
    text = text.lower()

    if any(word in text for word in ["hi", "hello", "hey", "salam", "assalam"]):
        return "Welcome to ZAIQA! I can help with menu, prices, delivery, reservations, and more."

    elif any(word in text for word in ["menu", "food", "khaana"]):
        return "Our menu includes Desi Mains (Karahi, Nihari, Haleem, Sajji), BBQ, Burgers, Rice, Deals, Beverages & Desserts."

    elif any(word in text for word in ["price", "kitna", "cost"]):
        return "Prices: Desi Mains 800–2500, BBQ 600–1800, Burgers 400–900, Rice 350–1200."

    elif any(word in text for word in ["deliver", "ghar", "area"]):
        return "Delivery: Lahore/Karachi/Islamabad 30–45 mins, other areas 60–90 mins. PKR 100 fee, free above 1500."

    elif any(word in text for word in ["book", "reserve", "table"]):
        return "Tables available for 2–20 people. Book 2 hours in advance."

    elif any(word in text for word in ["open", "hours", "timing"]):
        return "Mon–Thu 12–12, Fri 1–1, Sat–Sun 11–1 AM."

    elif any(word in text for word in ["pay", "jazzcash", "easypaisa"]):
        return "We accept JazzCash, EasyPaisa, Card, Bank Transfer, COD."

    elif any(word in text for word in ["deal", "offer", "discount"]):
        return "Deals updated every Monday. Follow @zaiqaeats."

    elif any(word in text for word in ["order", "status", "track"]):
        return "Send your order ID or phone number to track your order."

    else:
        return "Our team will follow up shortly. Follow @zaiqaeats for updates."