class Artist:
    def __init__(self, name, year_of_birth):
        self._name = name
        self._year_of_birth = year_of_birth

    def name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def year_of_birth(self):
        return self._year_of_birth

    def set_year_of_birth(self, new_year_of_birth):
        self._year_of_birth = new_year_of_birth

    def description(self):
        return f"{self._name} was born in {self._year_of_birth}"
