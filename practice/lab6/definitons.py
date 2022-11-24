class Object:
    pass


class Person:
    def __init__(self, fname, lname, age=0):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def introduce(self):
        """ Object introduces itself"""
        return f"My name is {self.first_name} and my last name is {self.last_name}"
