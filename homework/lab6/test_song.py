from song import Song


def test_song_name():
    song = Song("Eminem", "Rap God", 369)
    assert song.name() == "Rap God"


def test_song_set_name():
    song = Song("Eminem", "Rap God", 369)
    song.set_name("Without Me")
    assert song.name() == "Without Me"


def test_song_artist():
    song = Song("Eminem", "Rap God", 369)
    assert song.artist() == "Eminem"


def test_song_set_artist():
    song = Song("Eminem", "Rap God", 369)
    song.set_artist("Quebonafide")
    assert song.artist() == "Quebonafide"


def test_song_length():
    song = Song("Eminem", "Rap God", 369)
    assert song.length() == 369


def test_song_set_length():
    song = Song("Eminem", "Rap God", 369)
    song.set_length(669)
    assert song.length() == 669
