# Для повышения читаемости кода, максимальная длина строки была повышена до 99 символов.

# Импортируем все необходимые библиотеки, в соответствии с PEP8.
import telebot
import requests
from config import token

# Инициализируем экземпляр объекта 'TeleBot' из библиотеки 'telebot', с токеном {token}.
bot = telebot.TeleBot(token=token)


@bot.message_handler(commands=["coffee"])
def mess_handler_1(message: telebot.types.Message) -> None:
    """
    Функция обработчик команды '/coffee'.

    :param message: Объект telegtam-сообщения
    :type message: telebot.types.Message
    :return type: None
    """

    # Отправляем запрос на сайт.
    response = requests.get(url="https://coffee.alexflipnote.dev/random.json")

    # Если статус HTTPS запроса = 200 (Если запрос обработан верно).
    if response.status_code == 200:

        # Получаем json данные HTTPS ответа в виде словаря.
        data = response.json()

        # Получаем url-адрес случайного изображения кофе.
        photo = data["file"]

        # Отправляем пользователю изображение.
        bot.send_photo(
            message.chat.id,
            photo=photo
        )
    else:
        bot.send_message(
            message.chat.id,
            text="Возможно, на сервере произошла ошибка."
        )


# Запускает бота, если происходит запуск скрипта как основного файла, а не как библиотеки.
if __name__ == "__main__":
    bot.polling(non_stop=True)
