from config import *
import telebot
from logic import generate_image

API_TOKEN = '8285421568:AAEQcdQwTLxyeHbpLFlirY0aIUrHKaItEGs'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привет!
Я бот, который будет генерировать изображения для каждого твоего сообщения( под каждым я имею ввиду абсолютно каждое )
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def gener_img(message):
    try:
        bot.reply_to(message, "🎨 Генерирую изображения, прошу подождать и набраться терпения... В противном случае, проваливайте отсюда.")
        prompt = message.text
        image_url = generate_image(prompt)

        bot.send_photo(message.chat.id, image_url, caption = "Готово! Вот твое изображение и проваливай")
    except Exception as e:
        bot.reply_to(message, f'ХАХААХАХХ тут проблемка появилась. Фото не сгенерировалась: {e}')

bot.infinity_polling()