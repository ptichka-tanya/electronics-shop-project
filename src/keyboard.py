from src.item import Item


class MixinLang:
    """
    Миксин-класс для хранения и изменения раскладки клавиатуры.
    """

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Меняет язык ввода на клавиатуре"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLang):
    """
    Класс для представления товара “клавиатура” в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
