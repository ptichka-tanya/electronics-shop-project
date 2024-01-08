from src.item import Item

item1 = Item("Смартфон", 10000, 20)

Item.pay_rate = 0.75

assert Item.all == [item1]


def test_calculate_total_price():
    assert item1.price * item1.quantity == 200000
    assert item1.calculate_total_price() == 200000


def test_apply_discount():
    assert item1.price * Item.pay_rate == 7500

    item1.apply_discount()
    assert item1.price == 7500
