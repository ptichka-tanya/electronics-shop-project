from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Парогенератор", 200, 5)

Item.pay_rate = 0.75

assert Item.all == [item1, item2]


def test_item_repr():
    assert repr(item2) == "Item('Парогенератор', 200, 5)"


def test_item_str():
    assert str(item2) == 'Парогенератор'


def test_calculate_total_price():
    assert item1.price * item1.quantity == 200000
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    assert item1.price * Item.pay_rate == 7500

    item1.apply_discount()
    assert item1.price == 7500


def test_name_property():
    assert item1.name == "Смартфон"
    assert item2.name == "Парогенератор"


def test_name_setter():
    item1.name = 'Смартфон'
    assert item1.name == 'Смартфон'
    item2.name = 'Парогенератор'
    assert item2.name == 'Парогенера'


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')

    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[3].price == 50
    assert Item.all[1].quantity == 3


def test_string_to_number():
    assert Item.string_to_number("4.27465") == 4
