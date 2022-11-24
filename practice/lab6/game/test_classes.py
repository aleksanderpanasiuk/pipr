from classes import Player
import pytest


def test_create_player():
    player = Player("Jurek Ogorek")
    assert player.name() == "Jurek Ogorek"


def test_compare_players():
    jurek = Player("Jurek Ogorek")
    inny_jurek = Player("Jurek Ogorek")
    karolina = Player("Karolina Malina")

    assert not (jurek == karolina)
    assert jurek.name() == inny_jurek.name()


def test_create_player_with_lives():
    player = Player("Jurek Ogorek", 4)
    assert player.name() == "Jurek Ogorek"
    assert player.lives == 4


def test_introduce():
    player = Player("Jurek Ogorek", 3)
    assert player.info() == "My name is Jurek Ogorek. I have 3 lives left."

    player = Player("Jurek Ogorek", 1)
    assert player.info() == "My name is Jurek Ogorek. I have 1 life left."


def test_introduce_as_str():
    player = Player("Jurek Ogorek", 3)
    assert str(player) == player.info()

    player = Player("Jurek Ogorek", 1)
    assert str(player) == player.info()


def test_set_name():
    player = Player("Jurek Ogorek", 3)
    assert player.name() == "Jurek Ogorek"
    player.set_name("Karolina Malina")
    assert player.name() == "Karolina Malina"


def test_set_name_empty():
    player = Player("Jurek Ogorek", 3)
    with pytest.raises(ValueError):
        player.set_name("")


def test_set_name_lowercase():
    player = Player("jurek ogorek", 3)
    player.set_name("jurek ogorek")

    assert player.name() == "Jurek Ogorek"
