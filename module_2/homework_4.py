class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("The `make_sound` method must be overridden in child classes!")


class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        print("Гав")


class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def make_sound(self):
        print("Мяу")


# Пример использования
dog = Dog(name="Ben", species="Dog")
print(f"{dog.name}: ", end="")
dog.make_sound()

cat = Cat(name="Tom", species="Cat")
print(f"{cat.name}: ", end="")
cat.make_sound()
