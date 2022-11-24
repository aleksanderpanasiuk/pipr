from planets import Planet
import pytest


def test_planet_name():
    planet = Planet(3, 0, 0,  no_moons=1)
    assert planet.name() == ""

    planet.set_name("Ziemia")
    assert planet.name() == "Ziemia"


def test_planet_name_not_stringable():
    with pytest.raises(ValueError):
        planet = Planet(3, 0, 0, name=(1, 4, 2))
        planet.name()


def test_planet_position():
    planet = Planet(3, 0, 0,  "Ziemia", no_moons=1)
    assert planet.position() == (3, 0, 0)

    planet.set_position((2, 1, 3))
    assert planet.position() == (2, 1, 3)


def test_planet_position_nan():
    with pytest.raises(ValueError):
        planet = Planet(3, "mars", 0,  "Ziemia", no_moons=1)
        planet.position()


def test_planet_no_moons():
    planet = Planet(3, 1, 0,  "Ziemia")
    assert planet.number_of_moons() == 0

    planet.set_number_of_moons(4)
    assert planet.number_of_moons() == 4


def test_planet_no_moons_innit():
    planet = Planet(3, 1, 0,  "Ziemia", 31)
    assert planet.number_of_moons() == 31
