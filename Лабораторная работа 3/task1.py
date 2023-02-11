class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}"  # добавил везде двоеточия для красоты))

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self._pages = value

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. {self.pages} c."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: float):
        if not isinstance(value, float):
            raise TypeError
        if value <= 0:
            raise ValueError
        self._duration = value

    def duration_string(self):
        """Метод чтобы представить длительность в виде строки с разбиением на часы, минуты и секунды"""
        hours = int(self.duration // 1)
        minutes = int((self.duration - hours) * 60)
        sec = round((((self.duration - hours) * 60)-minutes)*60)
        return f"{hours} ч. {minutes} мин. {sec} с."

    def __str__(self):
        return f"Книга: {self.name}. Автор: {self.author}. Длительность: {self.duration_string()} "

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


audio_book1 = AudioBook("Ведьмак", "А. Сапковский", 2.1416)
print(audio_book1)
paper_book1 = PaperBook("Ведьмак", "А. Сапковский", 563)
print(paper_book1)
audio_book2 = AudioBook("Ведьмак", "А. Сапковский", -0.011)
print(audio_book2)
paper_book2 = PaperBook("Ведьмак", "А. Сапковский", "ee")
print(paper_book2)