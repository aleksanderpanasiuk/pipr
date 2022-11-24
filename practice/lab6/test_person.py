from definitons import Person


def test_init():
    person = Person("First", "Last")
    assert person.first_name == "First"
    assert person.last_name == "Last"


def test_init_with_age():
    person = Person("First", "Last", 18)
    assert person.first_name == "First"
    assert person.last_name == "Last"
    assert person.age == 18
