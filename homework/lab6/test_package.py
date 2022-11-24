from package import Package
import pytest


def test_package_sender():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    assert package.sender() == "abc 12"


def test_package_set_sender():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    package.set_sender("wwa 222")

    assert package.sender() == "wwa 222"


def test_package_set_sender_not_str():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)

    with pytest.raises(ValueError):
        package.set_sender(123)


def test_package_reciever():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    assert package.reciever() == "das 31"


def test_package_set_reciever():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    package.set_reciever("wro 55")
    assert package.reciever() == "wro 55"


def test_package_set_reciever_not_str():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)

    with pytest.raises(ValueError):
        package.set_reciever(123)


def test_package_dimensions():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    assert package.dimensions() == (21, 3, 7)


def test_package_set_dimensions():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    package.set_dimensions((1, 1, 1))
    assert package.dimensions() == (1, 1, 1)


def test_package_weight():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    assert package.weight() == 2


def test_package_set_weight():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    package.set_weight(4)
    assert package.weight() == 4


def test_package_smallest_dimenstion():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    assert package.smallest_dimension() == 3


def test_package_biggest_dimenstion():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    assert package.biggest_dimension() == 21


def test_package_description():
    package = Package("abc 12", "das 31", (21, 3, 7), 2)
    result = "Package sent from abc 12 to das 31 weights 2 kg"
    result += " and its biggest dimension is 21 and smallest is 3"
    assert package.description() == result
