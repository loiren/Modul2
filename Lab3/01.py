class Book:
    """ Базовый класс книги.
    Атрибуты:
        _name (str): Название книги (приватный атрибут).
        _author (str): Автор книги (приватный атрибут).
    """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self):
        """Возвращает строковое представление объекта (для пользователя)."""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """Возвращает строковое представление объекта (для отладки)."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """
        Класс для представления печатной книги, наследует от Book.

        Атрибуты:
            pages (int): Количество страниц в книге.
        """

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализирует новый объект PaperBook.

            name (str): Название книги.
            author (str): Автор книги.
            pages (int): Количество страниц.

        Raises:
            ValueError: Если количество страниц не является целым положительным числом.
        """

        super().__init__(name, author)
        if not isinstance(pages, int) or pages <= 0:
            raise ValueError("Количество страниц должно быть целым положительным числом.")
        self.pages = pages

    def __str__(self):
        """Возвращает строковое представление объекта (для пользователя)."""
        return f"{super().__str__()} .Количество страниц: {self.pages}"

    def __repr__(self):
        """Возвращает строковое представление объекта (для отладки)."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

class AudioBook(Book):
    """
        Класс для представления аудиокниги, наследует от Book.

        Атрибуты:
            duration (float): Продолжительность аудиокниги в минутах.
        """

    def __init__(self, name: str, author: str, duration: float):
        """
                Инициализирует новый объект AudioBook.

                    name (str): Название книги.
                    author (str): Автор книги.
                    duration (float): Продолжительность аудиокниги в минутах.

                Raises:
                     ValueError: Если продолжительность не является положительным числом.
                """
        super().__init__(name, author)
        if not isinstance(duration, (int, float)) or duration <= 0:
             raise ValueError("Продолжительность должна быть положительным числом.")
        self.duration = duration

    def __str__(self):
        """Возвращает строковое представление объекта (для пользователя)."""

        return f"{super().__str__()} .Продолжительность: {self.duration} минут"

    def __repr__(self):
        """Возвращает строковое представление объекта (для отладки)."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"