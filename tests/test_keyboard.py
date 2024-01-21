import pytest

from src.keyboard import Keyboard


@pytest.fixture
def kb():
    return Keyboard("Xiaomi Keyboard Pro", 20_000, 10)


def test_init(kb):
    assert str(kb) == "Xiaomi Keyboard Pro"
    assert str(kb.language) == "EN"


def test_change_lang(kb):
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
    with pytest.raises(AttributeError):
        kb.language = 'JP'
