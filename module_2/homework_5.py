import os


class SimplestFileManager:
    """
    Простейший Файловый Менеджер.
    Позволяет создавать и вносить изменения в файл, а затем выводить его содержимое.

    Attributes:
        file_name (str): Имя файла (вместе с расширением)
        current_dir (str): Текущая директория
        file_path (str): Путь файла
    """

    def __init__(self, file_name: str):
        """
        Инициализатор объекта фалового менеджера.

        Args:
            file_name (str): Имя файла (вместе с расширением)
        """

        self.file_name = file_name
        self.current_dir = os.curdir
        self.file_path = os.path.join(self.current_dir, self.file_name)

    def write_on_file(self, text: str) -> None:
        """
        Создаёт файл в текущей директории и изменяет его содержимое.

        Args:
            text (str): Текст, который будет записан в файл
        """

        with open(self.file_path, "w") as file:
            file.write(text)

    def read_file(self) -> str:
        """
        Считывает содержимое файла и его возвращет в виде строки.

        Returns:
            str: Содержимое файла
        """

        with open(self.file_path, "r") as file:
            text_file = file.read()
        return text_file


# Пример использования
fm = SimplestFileManager(file_name="sample.txt")
fm.write_on_file("Hellow, World!")

print(fm.read_file())
