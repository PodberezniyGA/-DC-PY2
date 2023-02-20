class Car:
    def __init__(self, brand: str, pwr: float):
        """
        Создание объекта класса автомобиль
        :param brand: марка автомобиля
        :param pwr: мощность автомобиля (в л.с.)
        Примеры:
        >>> test_car = Car("Cadillac", 241)  #Инициализация объекта класса
        """
        self.brand = brand  # марка автомобиля
        self.pwr = pwr
        self._comm = None  # Комментарий к автомобилю, по умолчанию отсутствует, для добавления применить метод add_comm
        self._overall = None  # Общая оценка автомобиля

    def add_comm(self, message: str):
        """
        Метод, позволяющий оставить комментарий к автомобилю
        :param message:
        :return:
        Примеры:
        >>> test_car = Car("Cadillac", 241)  #Инициализация объекта класса
        >>> test_car.add_comm("Автомобиль с пробегом, аварий не было")
        """
        self._comm = message

    def write_com(self):
        """
        Метод, позволяющий вернуть ранее оставленный комментарий к автомобилю
        :return: возвращает комментарий
        Примеры:
        >>> test_car = Car("Cadillac", 241)  #Инициализация объекта класса
        >>> test_car.add_comm("Автомобиль с пробегом, аварий не было")
        >>> test_car.write_com()
        'Автомобиль с пробегом, аварий не было'
        """
        return self._comm

    def add_overall(self, rating: float):
        """
        Метод, позволяющий добавить общую оценку автомобиля
        :param rating: оценка автомобиля (от 0 до 10)
        Примеры:
        >>> test_car = Car("Cadillac", 241)
        >>> test_car.add_overall(9.3)
        """

        if isinstance(rating, float):
            if 10. >= rating >= 0.:
                self._overall = rating
            else:
                raise ValueError("overall must be from 0 to 10")
        else:
            raise TypeError("overall must be float")

    def check_overall(self):
        """
        Метод, печатающий общую оценку автомобиля. Предварительно необходимо добавить её к экземпляру класса
        Примеры:
        >>> test_car = Car("Cadillac", 241)
        >>> test_car.add_overall(9.3)
        >>> test_car.check_overall()
        Общая оценка автомобиля: 9.3
        """
        print(f'Общая оценка автомобиля:{self._overall}')

    @property
    def power(self):
        """
        Геттер для атрибута (мощности) автомобиля
        :param self:
        :return:
        """
        return self._power

    @power.setter  # Мощность автомобиля должна быть положительным числом, поэтому создан атрибут
    def power(self, pwr: float):
        """
        Cеттер для атрибута (мощности) автомобиля
        :param self:
        :param pwr: мощность автомобиля
        :return:
        """
        if isinstance(pwr, float):
            if pwr > 0:
                self._power = pwr
            else:
                raise ValueError(f'power of auto must be greater than zero, while incoming {pwr}')
        else:
            raise ValueError(f'power must be float, while incoming is {type(pwr)}')

    def __str__(self):
        """
        :return: Возвращает марку и мощность автомобиля
        Примеры:
        >>> test_car = Car("Cadillac", 241)
        >>> print(test_car)
        Автомобиль "Cadillac", мощность 241
        """
        return f'Автомобиль "{self.brand}", мощность {self.power}'

    def __repr__(self):
        """
        :return:
        Примеры:
        >>> test_car = Car("Cadillac", 241)
        >>> repr(test_car)
        "Car(brand='Cadillac', power=241)"
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, pwr={self.power})"


class OffroadCar(Car):
    def __init__(self, brand: str, pwr: int, year: int):
        """
        Создание объекта класса внедорожник
        :param brand: марка автомобиля
        :param pwr:  мощность автомобиля
        :param year: год производства автомобиля
        Примеры:
        >>> test_film = OffroadCar("JeepWrangler", 200, 2018) # инициализация объекта класса
        """
        super().__init__(brand, pwr)  # марка и мощность наследуются
        self.year = year
        self._comm = None
        self._overall = None

    def __str__(self):  # Перегрузка необходима в связи с добавлением "OffroadCar" и параметра (год)
        """
        :return: Возвращает марку и мощность автомобиля
        Примеры:
        >>> test_car = OffroadCar("JeepWrangler", 200, 2018)
        >>> print(test_car)
        Автомобиль класса внедорожник "JeepWrangler", мощность 200, 2018 год
        """
        return f'Автомобиль класса внедорожник "{self.brand}", длительность {self.power}, {self.year} год'

    def __repr__(self):  # Перегрузка необходима ради введения в метод нового параметра (год)
        """
        Магический метод, выдающий строку, необходимую для инициализации автомобиля класса внедорожник
        :return:
        Примеры:
        >>> test_car = OffroadCar("JeepWrangler", 200, 2018)
        >>> print(repr(test_car))
        OffroadCar(name='JeepWrangler', power=200, year=2018)
        """
        return f"{self.__class__.__name__}(brand={self.brand!r}, pwr={self.power}, year = {self.year})"

    def check_overall(self):  # методу необходима перегрузка, чтобы показывать общую оценку автомобиля
        """
        Метод, печатающий общую характеристику автомобиля, ранее добавленную
        методом add_overall
        Примеры:
        >>> test_car = OffroadCar("JeepWrangler", 200, 2018)
        >>> test_car.add_overall(8.5)
        >>> test_car.check_overall()
        Общая характеристика автомобиля класса внедорожник:8.5
        """
        print(f'Общая характеристика автомобиля класса внедорожник:{self._overall}')


if __name__ == "__main__":
    """
    Унаследованы методы add_overall, add_comm и write_comm. Метод check_overall перегружен
    """
    pass
