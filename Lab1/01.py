import doctest

# TODO Написать 3 класса с документацией и аннотацией типов

class Lampa:
    def __init__(self, color: int, power: int, dimmer: int):
        """
        Создание и подготовка к работе объекта "Лампа"

        :param color: температура света в кельвинах
        :param power: Мощность лампы в ватах
        :param dimmer: Мощность свечения лампы в ватах

        Примеры:
        >>> lampa = Lampa(4200, 15, 15)  # инициализация экземпляра класса
        """
        if not isinstance(color, int):
            raise TypeError("Температура света должна быть типа int")
        if color <= 0:
            raise ValueError("Температура света должна быть положительным числом")
        self.color = color

        if not isinstance(power, int):
            raise TypeError("Мощность лампы должна быть int")
        if power < 0:
            raise ValueError("Мощность лампы не может быть отрицательным числом")
        self.power = power

        if not isinstance(dimmer, int):
            raise TypeError("Мощность свечения лампы должна быть int")
        if dimmer < 0:
            raise ValueError("Мощность свечения лампы не может быть отрицательным числом")
        self.dimmer = dimmer

    def lampa_is_power_off(self) -> bool:
        """
        Функция которая проверяет включена или выключена лампа

        :return: Лампа выключена

        Примеры:
        >>> lampa = Lampa(4200, 15, 0)
        >>> lampa.lampa_is_power_off()
        """
        ...

    def add_power(self, watt: (int, float)) -> None:
        """
        Увеличение мощности лампы.
        :param watt: Мощность свечения лампы

        :raise ValueError: Если добавленная мощность свечения лампы больше номинальной мощности лампы, то вызываем ошибку

        Примеры:
        >>> lampa = Lampa(4200, 15, 0)
        >>> lampa.add_power(15)
        """
        if not isinstance(watt, (int, float)):
            raise TypeError("Мощность свечения лампы должна быть типа int или float")
        if watt < 0:
            raise ValueError("Мощность свечения лампы должна положительным числом")
        ...

    def reduce_power(self, reducing_power: (int, float)) -> None:
        """
        Уменьшение мощность свечения лампы.

        :param reducing_power: параметр мощности свечения лампы

        :raise ValueError: Если параметр мощности свечения лампы превышает текущую мощность свечения лампы,
        то возвращается ошибка.

        Примеры:
        >>> lampa = Lampa(4200, 15, 15)
        >>> lampa.reduce_power(10)
        """
        if not isinstance(reducing_power, (int, float)):
            raise TypeError("Мощность свечения лампы должна быть типа int или float")
        if reducing_power < 0:
            raise ValueError("Мощность свечения лампы должна положительным числом")
        ...


class Steklo:
    def __init__(self, prozrachnost: float, prelomlenie: float, dispersiya: float):
        """
        Создание и подготовка к работе объекта материала "Стекло" для использования в 3д моделировании

        :param prozrachnost: коэфициент прозрачности
        :param prelomlenie: коэфициент преломления
        :param dispersiya:  коэфициент дисперсии

        Примеры:
        >>> steklo = Steklo(240, 1.55, 0.15) # инициализация экземпляра класса
        """

        if not isinstance(prozrachnost, (int, float)):
            raise TypeError("коэфициент прозрачности должен быть типа float")
        if prozrachnost <= 0:
            raise ValueError("коэфициент прозрачности должен быть положительным числом")
        self.prozrachnost = prozrachnost

        if not isinstance(prelomlenie, (int, float)):
            raise TypeError("коэфициент преломления должен быть float")
        if prelomlenie < 0:
            raise ValueError("коэфициент преломления не может быть отрицательным числом")
        self.prelomlenie = prelomlenie

        if not isinstance(dispersiya, (int, float)):
            raise TypeError("коэфициент дисперсии должен быть float")
        if dispersiya < 0:
            raise ValueError("коэфициент дисперсии не может быть отрицательным числом")
        self.dispersiya = dispersiya

    def mate(self, proz: float) -> None:
        """
        Изменение и проверка степени прозрачности стекла
        :param proz: коэфициент прозрачности

        :raise ValueError: Если коэфициент прозрачности не соответствует эталонному, то вызываем ошибку

        Примеры:
        >>> steklo = Steklo(240, 1.55, 0.15)
        >>> steklo.mate(140)
        """
        if not isinstance(proz, (int, float)):
            raise TypeError("коэфициент прозрачности должен быть типа float")
        if proz < 0:
            raise ValueError("коэфициент прозрачности должен положительным числом")
        ...

    def prism(self, disper: float) -> None:
        """
        Изменение и проверка коэфициент дисперсии стекла

        :param disper: коэфициент дисперсии

        :raise ValueError: Если коэфициент дисперсии не соответствует эталонному, то возвращается ошибка.

        Примеры:
        >>> steklo = Steklo(240, 1.55, 0.15)
        >>> steklo.prism(0.5)
        """
        if not isinstance(disper, (int, float)):
            raise TypeError("коэфициент прозрачности должен быть типа float")
        if disper < 0:
            raise ValueError("коэфициент прозрачности должен положительным числом")
        ...


class Paket_Chips:
    def __init__(self, firma: str, vkus: str, volume: float):
        """
        Создание и подготовка к работе объекта "Пакет чипсов"

        :param firma: изготовитель
        :param vkus: вкус чипсов
        :param volume: объем пакета (вес в граммах)

        Примеры:
        >>> chips = Paket_Chips("Вкусняшки", "Лук с чисноком", 150) # инициализация экземпляра класса
        """

        if not isinstance(firma, str):
            raise TypeError("параметр изготовитель должен быть типа str")
        self.firma = firma

        if not isinstance(vkus, str):
            raise TypeError("параметр вкус должен быть типа str")
        self.vkus = vkus

        if not isinstance(volume, (int, float)):
            raise TypeError("параметр объем пакета должен быть типа int или float")
        if volume < 0:
            raise ValueError("параметр объем пакета не может быть отрицательным числом")
        self.volume = volume

    def is_empty_Paket_Chips(self) -> bool:
        """
        Проверка а есть ли вообще чипсы в пакете

        :return: В пакете есть чипсы

        Примеры:
        >>> paket = Paket_Chips("Вкусняшки", "Лук с чисноком", 150)
        >>> paket.is_empty_Paket_Chips()
        """
        ...

    def remove_chips(self, estimate_chips: float) -> None:
        """
        Едим вкусные чипсы.

        :param estimate_chips: сколько чипсов сьели
        :raise ValueError: Если количество сьеденых чипсов превышает количество чипсов в пакете,
        то возвращается ошибка.

        :return: сколько чипсов сьели

        Примеры:
        >>> chips = Paket_Chips("Вкусняшки", "Лук с чисноком", 150)
        >>> chips.remove_chips(100)
        """
        if not isinstance(estimate_chips, (int, float)):
            raise TypeError("количество сьеденых чипсов должно быть типа int или float")
        if estimate_chips < 0:
            raise ValueError("количество сьеденых чипсов должно быть положительным числом")
        ...



if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass