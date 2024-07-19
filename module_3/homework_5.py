# Для повышения читаемости кода, максимальная длина строки была повышена до 99 символов.

# Также немного изменена исходная логика:
# Инициализация 'win_value' происходит во время инициализации кнопок,
# в обработчике команды '/start', а не в обработчике callback'ов.
# Чтобы эта игра не была похожа на казино и 'win_value' было известно заранее. :)

# Импортируем все необходимые библиотеки, в соответствии с PEP8.
import random
import telebot
from config import token

# Инициализируем экземпляр объекта 'TeleBot' из библиотеки 'telebot', с токеном {token}.
bot = telebot.TeleBot(token=token)

# Инициализируем начальное победное значение.
win_value = None


@bot.message_handler(commands=["start"])
def mess_handler_1(message: telebot.types.Message) -> None:
    """
    Функция обработчик команды '/start'.

    :param message: Объект telegtam-сообщения
    :type message: telebot.types.Message
    :return type: None
    """

    global win_value

    # Создаём разметку для последующего размещения inline-кнопок.
    markup = telebot.types.InlineKeyboardMarkup()

    # Создаём и заполняем список inline-кнопок.
    buttons = []
    for var in range(0, 4 + 1):
        buttons.append(telebot.types.InlineKeyboardButton(text="🔥", callback_data=str(var)))

    # Размещаем inline-кнопки в 1 строку.
    markup.row(*buttons)

    # Отправляем пользователю сообщение, с прикреплённой разметкой.
    bot.send_message(
        message.chat.id,
        text="Что выберешь?",
        reply_markup=markup
    )

    # Инициализируем победное значение случайным целым числом в интервале [0; 4].
    win_value = random.randint(0, 4)


@bot.callback_query_handler(func=lambda callback: True)
def callbacks_handler_1(callback: telebot.types.CallbackQuery) -> None:
    """
    Функция обработчик callback'ов
    :param callback: Запрос обратного вызова
    :type callback: telebot.types.CallbackQuery
    :return type: None
    """

    global win_value

    if int(callback.data) == win_value:
        bot.send_message(callback.message.chat.id, text="Поздравляю, ты победил 💲")
    else:
        bot.send_message(callback.message.chat.id, text="Увы, ты проиграл 😩")


# Запускает бота, если происходит запуск скрипта как основного файла, а не как библиотеки.
if __name__ == "__main__":
    bot.polling(non_stop=True)
