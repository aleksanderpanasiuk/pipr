class Planet:
    def __init__(self, x, y, z, name="", no_moons=0):
        self._position = (x, y, z)
        self._name = name
        self._number_of_moons = no_moons

    def name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def position(self):
        return self._position

    def set_position(self, new_position):
        self._position = new_position

    def number_of_moons(self):
        return self._number_of_moons

    def set_number_of_moons(self, new_no_moons):
        self._number_of_moons = new_no_moons
