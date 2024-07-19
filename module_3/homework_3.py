# Для повышения читаемости кода, максимальная длина строки была повышена до 99 символов.

# Импортируем все необходимые библиотеки, в соответствии с PEP8.
import telebot
from config import token

# Инициализируем экземпляр объекта 'TeleBot' из библиотеки 'telebot', с токеном {token}.
bot = telebot.TeleBot(token=token)


@bot.message_handler()
def mess_handler_1(message: telebot.types.Message) -> None:
    """
    Функция обработчик всех сообщений.

    :param message: Объект telegtam-сообщения
    :type message: telebot.types.Message
    :return type: None
    """

    # Построчно разбиваем текст сообщения.
    text_lst = message.text.split("\n")

    # Если в тексте сообщения от 3 до 11 строк включительно.
    if len(text_lst) in range(3, 11 + 1):

        # Отправляем пользователю опрос.
        bot.send_poll(
            message.chat.id,
            question=text_lst[0],
            options=list(map(telebot.types.InputPollOption, text_lst[1::]))
        )
    else:
        # Отправляем пользователю соответствующее сообщение.
        bot.send_message(
            message.chat.id,
            text="В вашем сообщении должно быть от 3 до 11 строк"
        )


# Запускает бота, если происходит запуск скрипта как основного файла, а не как библиотеки.
if __name__ == "__main__":
    bot.polling(non_stop=True)
