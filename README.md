Telegram QR Code Generator Bot

Instantly convert any link into a QR code via Telegram

---

 Project Overview  
A lightweight Telegram bot that transforms URLs into QR codes with a simple message. Built with Python and the Telebot framework, it's perfect for quickly generating scannable codes without leaving your chat.

---

 Key Features  
✨ Instant Conversion  
- Send any valid URL to get a QR code image reply  
- Supports all common link formats (http/https)  

⚡ Lightning-Fast  
- Asynchronous processing for near-instant responses  
- Optimized QR code generation (15x scaling for readability)  

🔒 Secure Handling  
- No logging or storage of user-submitted URLs  
- Configuration via secure `config.json` file  

---

 Tech Stack  
- Core Framework: Telebot (async version)  
- QR Generation: `pyqrcode` + `pypng`  
- Dependencies:  
  - `telebot`  
  - `pyqrcode`  
  - `asyncio`  

---

 Setup Instructions  

1. Create `config.json`  
   ```json
   {
     "API_TOKEN": "YOUR_TELEGRAM_BOT_TOKEN"
   }
   ```

2. Install dependencies  
   ```bash
   pip install telebot pyqrcode pypng
   ```

3. Run the bot  
   ```bash
   python bot.py
   ```

---

 Usage Example  
1. Start the bot: `/start`  
2. Send any URL:  
   ```text
   https://github.com
   ```  

---

 Contribution Ideas  
- Add error handling for invalid URLs  
- Implement QR code customization (colors/sizes)  
- Create a web dashboard interface  
- Add analytics tracking for generated codes  
