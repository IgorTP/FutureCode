import telebot
from config import token

bot = telebot.TeleBot(token=token)


@bot.message_handler(content_types=["text"])
def func(message: telebot.types.Message):
    output_data = message.text * 10
    bot.send_message(message.from_user.id, output_data)


if __name__ == "__main__":
    bot.polling(non_stop=True)
