class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка автомобиля: {self.make}")
        print(f"Модель автомобиля: {self.model}")
        print(f"Год выпуска: {self.year}")


# Пример использования
car = Car(make="Nissan", model="Qashqai", year=2022)
car.display_info()
