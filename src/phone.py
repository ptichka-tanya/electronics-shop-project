from src.item import Item


class Phone(Item):
    """Дочерний класс класса Item для представления данных о телефонах в магазине"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Отображает информацию об объекте класса в режиме отладки (для разработчиков)"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim <= 0:
            assert ValueError("Количество сим-карт должно быть целым неотрицательным числом.")
        else:
            if number_of_sim is float:
                assert ValueError("Количество сим-карт должно быть целым неотрицательным числом.")
            else:
                self.__number_of_sim = number_of_sim
