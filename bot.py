import telebot
import os
import time
from logic import generate_image

API_TOKEN = ''

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(
        message,
        """Привет! 🎨
Я бот, который генерирует изображения для каждого твоего сообщения.
Просто напиши мне, что ты хочешь увидеть, и я создам это для тебя!
"""
    )

@bot.message_handler(func=lambda message: True)
def gener_img(message):
    try:
        msg = bot.reply_to(message, "🎨 Генерирую изображение... Пожалуйста, подождите.")

        prompt = message.text

        image_url = generate_image(prompt, filename="result.jpg")

        bot.delete_message(message.chat.id, msg.message_id)

        bot.send_photo(message.chat.id, open("result.jpg", "rb"), caption="Вот ваше изображение!")
        
        os.remove("result.jpg")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при генерации изображения: {e}")

bot.infinity_polling()
