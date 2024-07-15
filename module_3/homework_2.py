# Для повышения читаемости кода, максимальная длина строки была повышена до 99 символов.

# Импортируем все необходимые библиотеки, в соответствии с PEP8.
# Корректная хронология импортов:
# 1) Импорты из стандартной библиотеки
# 2) Импорты из сторонних библиотек
# 3) Импорты модулей из текущего проекта
import random
import telebot
from config import token

# Инициализируем экземпляр объекта 'TeleBot' из библиотеки 'telebot', с токеном {token}.
bot = telebot.TeleBot(token=token)


def check_mess_on_random(message: telebot.types.Message) -> bool:
    """
    Функция для проверки, входит ли слово 'рандом' в текст нашего сообщения (с учётом регистра).

    :param message: Объект telegtam-сообщения
    :type message: telebot.types.Message
    :return: Результат работы функции
    :return type: bool
    """

    if 'рандом' in message.text:
        return True
    return False


@bot.message_handler(func=check_mess_on_random)
def mess_handler_1(message: telebot.types.Message) -> None:
    """
    Функция обработчик, которая срабатывает в том случае,
    если функция 'check_mess_on_random' возвращает 'True'.

    :param message: Объект telegtam-сообщения
    :type message: telebot.types.Message
    :return type: None
    """

    # Случайное число в интервале [0; 100]
    random_int_0_100 = random.randint(0, 100)

    # Отправляет пользователю случайное число
    bot.send_message(message.from_user.id, f"Случайное число: {random_int_0_100}")


@bot.message_handler(func=lambda message: not check_mess_on_random(message))
def mess_handler_2(message: telebot.types.Message) -> None:
    """
    Функция обработчик, которая срабатывает в том случае,
    если функция 'check_mess_on_random' возвращает 'False', not(False) => True

    :param message: Объект telegtam-сообщения
    :type message: telebot.types.Message
    :return type: None
    """

    # Отправляет пользователю его же сообщение (echo-bot)
    bot.send_message(message.from_user.id, message.text)


# Запускает бота, если происходит запуск скрипта как основного файла, а не как библиотеки.
if __name__ == "__main__":
    bot.polling(non_stop=True)
