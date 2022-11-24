from artist import Artist


def test_artist_name():
    artist = Artist("Leonardo da Vinci", 1452)
    assert artist.name() == "Leonardo da Vinci"


def test_artist_set_name():
    artist = Artist("Leonardo da Vinci", 1452)
    artist.set_name("Leo")
    assert artist.name() == "Leo"


def test_artist_year_of_bith():
    artist = Artist("Leonardo da Vinci", 1452)
    assert artist.year_of_birth() == 1452


def test_artist_set_year_of_bith():
    artist = Artist("Leonardo da Vinci", 1452)
    artist.set_year_of_birth(2003)
    assert artist.year_of_birth() == 2003


def test_artist_description():
    artist = Artist("Leonardo da Vinci", 1452)
    result = "Leonardo da Vinci was born in 1452"
    assert artist.description() == result
