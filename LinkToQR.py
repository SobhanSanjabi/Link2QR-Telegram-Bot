from telebot.async_telebot import AsyncTeleBot
import telebot
import pyqrcode
import asyncio
import json
with open("config.json") as f:
    config = json.load(f)

API_TOKEN = config["API_TOKEN"]

bot = AsyncTeleBot(API_TOKEN)

# Handle '/start'
@bot.message_handler(commands=['start'])
async def start_bot(message):
    
    await bot.send_message(chat_id=message.chat.id,text="Hi.\nSend me any links, I transform it into QRCode.")

@bot.message_handler(func=lambda message:True)
async def getPic(message):
    url = message.text
    qr = pyqrcode.create(url)
    qr.png("Out.png",scale = 15)
    await bot.send_photo(message.chat.id,telebot.types.InputFile("Out.png"))
    
    
asyncio.run(bot.polling())
