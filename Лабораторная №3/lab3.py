class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """

        :param name: Название, тип str
        :param author: Автор, тип str
        """
        if not isinstance(name, str):
            raise TypeError('Значение name должно соответствовать типу str')
        self.name = name
        if not isinstance(author, str):
            raise TypeError('Значение author должно соответствовать типу str')
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        """

        :param name: Название, тип str
        :param author: Автор, тип str
        :param pages: Количество страниц, тип int
        """
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError('Значение pages должно соответствовать типу int')
        if not pages > 0:
            raise ValueError('Значение pages должно быть положительным числом')
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        """

        :param name: Название, тип str
        :param author:  Автор, тип str
        :param duration: Длительность проигрывания, тип float
        """
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError('Значение duration должно соответствовать типу float')
        if not duration > 0:
            raise ValueError('duration должно быть положительным числом')
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
