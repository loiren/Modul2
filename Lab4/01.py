class Animal:
    """
    Базовый класс, представляющий животное.

    Атрибуты:
    - name (str): Имя животного.
    - age (int): Возраст животного.
    - _species (str): Вид животного (инкапсулированный атрибут).
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Конструктор класса Animal.

        Аргументы:
        - name (str): Имя животного.
        - age (int): Возраст животного.
        - species (str): Вид животного.

        Исключения:
        - ValueError: Если имя или вид пустые, или возраст отрицательный.
        """
        if not name:
            raise ValueError("Имя животного не может быть пустым.")
        if not species:
            raise ValueError("Вид животного не может быть пустым.")
        if age < 0:
            raise ValueError("Возраст животного не может быть отрицательным.")

        self.name = name
        self.age = age
        self._species = species  # Инкапсулированный атрибут, так как вид животного не должен изменяться извне.

    def __str__(self) -> str:
        """
        Возвращает:
        - str: Строковое представление животного.
        """
        return f"{self.name} ({self._species}), возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает:
        - str: Формальное строковое представление животного.
        """
        return f"Animal(name={self.name}, age={self.age}, species={self._species})"

    def make_sound(self) -> str:
        """
        Возвращает:
        - str: Звук животного.
        """
        return "Неизвестный звук"

    def eat(self, food: str) -> str:
        """
        Метод, который описывает, как животное ест.

        Аргументы:
        - food (str): Еда, которую ест животное.

        Возвращает:
        - str: Сообщение о том, что животное ест.
        """
        return f"{self.name} ест {food}"

class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.

    Атрибуты:
    - breed (str): Порода собаки.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog.

        Аргументы:
        - name (str): Имя собаки.
        - age (int): Возраст собаки.
        - breed (str): Порода собаки.

        Исключения:
        - ValueError: Если порода пустая.
        """
        super().__init__(name, age, species="Собака")

        if not breed:
            raise ValueError("Порода собаки не может быть пустой.")

        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает:
        - str: Строковое представление собаки.
        """
        return f"{self.name} ({self.breed}), возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает:
        - str: Формальное строковое представление собаки.
        """
        return f"Dog(name={self.name}, age={self.age}, breed={self.breed})"

    def make_sound(self) -> str:
        """
        Возвращает:
        - str: Звук собаки.
        """
        return "Гав-гав!"

    def eat(self, food: str) -> str:
        """
        Перегруженный метод, так как собаки могут есть определенным образом.

        Аргументы:
        - food (str): Еда, которую ест собака.

        Возвращает:
        - str: Сообщение о том, как собака ест.
        """
        return f"{self.name} быстро съедает {food} и виляет хвостом!"

class Cat(Animal):
    """
    Дочерний класс, представляющий кошку.

    Атрибуты:
    - color (str): Цвет кошки.
    """

    def __init__(self, name: str, age: int, color: str) -> None:
        """
        Конструктор класса Cat.

        Аргументы:
        - name (str): Имя кошки.
        - age (int): Возраст кошки.
        - color (str): Цвет кошки.

        Исключения:
        - ValueError: Если цвет пустой.
        """
        super().__init__(name, age, species="Кошка")

        if not color:
            raise ValueError("Цвет кошки не может быть пустым.")

        self.color = color

    def __str__(self) -> str:
        """
        Возвращает:
        - str: Строковое представление кошки.
        """
        return f"{self.name} ({self.color}), возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает:
        - str: Формальное строковое представление кошки.
        """
        return f"Cat(name={self.name}, age={self.age}, color={self.color})"

    def make_sound(self) -> str:
        """
        Возвращает:
        - str: Звук кошки.
        """
        return "Мяу!"

    def eat(self, food: str) -> str:
        """
        Метод, который описывает, как кошка ест.

        Перегруженный метод, так как кошки едят медленно и аккуратно.

        Аргументы:
        - food (str): Еда, которую ест кошка.

        Возвращает:
        - str: Сообщение о том, как кошка ест.
        """
        return f"{self.name} медленно и аккуратно ест {food}."

animal = Animal("Неизвестное животное", 5, "Неизвестный вид")
dog = Dog("Бобик", 3, "Лабрадор")
cat = Cat("Мурка", 2, "Серый")

if __name__ == "__main__":
    # Вывод информации о животных
    print(animal)  # Неизвестное животное (Неизвестный вид), возраст: 5 лет
    print(dog)  # Бобик (Лабрадор), возраст: 3 лет
    print(cat)  # Мурка (Серый), возраст: 2 лет

    # Вызов методов
    print(animal.make_sound())  # Неизвестный звук
    print(dog.make_sound())  # Гав-гав!
    print(cat.make_sound())  # Мяу!

    # Вызов специфических методов
    print(dog.eat("мясо"))  # Бобик принес(ла) мяч
    print(cat.eat("рыбу"))
    pass
