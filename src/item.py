import csv
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки (для разработчиков)"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Отображает информацию об объекте класса для пользователей"""
        return f'{self.__name}'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[0:10]
        else:
            self.__name = name

    @classmethod
    def instantiate_from_csv(cls, file_path: str):
        """
        Класс-метод, инициализирующий экземпляры класса из файла.

        :param file_path: Путь к CSV-файлу с данными.
        :return: Экземпляры класса.
        """
        cls.all = []
        current_file_path = Path(__file__)
        file_path = current_file_path.parent.parent / file_path
        with open(file_path, 'r', newline='', encoding='windows - 1251') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], float(row['price']), int(row['quantity']))

    @staticmethod
    def string_to_number(string):
        """
        Преобразует строку в целое число.

        :param string: Строка, содержащая число.
        :return: Целое число.
        """
        return int(float(string))
