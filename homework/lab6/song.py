class Song:
    def __init__(self, artist, name, length):
        self._artist = artist
        self._name = name
        self._length = length

    def name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def artist(self):
        return self._artist

    def set_artist(self, new_artist):
        self._artist = new_artist

    def length(self):
        return self._length

    def set_length(self, new_length):
        self._length = new_length

    def description(self):
        return f"{self._name} by {self._artist} is {self._length} seconds long"
