from src.phone import Phone

phone1 = Phone("Xiaomi Redmi Note", 50_000, 5, 2)
phone2 = Phone("Samsung X5", 85_000, 7, 3)


def test_phone_repr():
    assert repr(phone1) == "Phone('Xiaomi Redmi Note', 50000, 5, 2)"


def test_number_of_sim():
    assert phone1.number_of_sim == 2
    assert phone2.number_of_sim == 3
