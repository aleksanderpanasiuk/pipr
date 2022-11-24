class Planet:
    def __init__(self, x, y, z, name="", no_moons=0):
        if self.check_pos((x, y, z)):
            raise ValueError("Position must be an integer")
        self._position = (x, y, z)

        if not isinstance(name, str):
            raise ValueError("Name must be str type")
        self._name = name

        self._number_of_moons = no_moons

    def name(self):
        return self._name

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise ValueError("Name must be str type")
        self._name = new_name

    def position(self):
        return self._position

    def set_position(self, new_position):
        if self.check_pos(new_position):
            raise ValueError("New position must be a tuple of integers")
        self._position = new_position

    def check_pos(self, pos):
        x, y, z = pos
        is_x_int = isinstance(x, int)
        is_y_int = isinstance(y, int)
        is_z_int = isinstance(z, int)

        return not (is_x_int and is_y_int and is_z_int)

    def number_of_moons(self):
        return self._number_of_moons

    def set_number_of_moons(self, new_no_moons):
        self._number_of_moons = new_no_moons
