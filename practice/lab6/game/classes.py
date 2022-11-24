class Player:
    """
    Class PLayer. Contains attributes:
    :param name: player's name
    :type name: str
    :param name: lives's name, defaults to 1
    :type name: int
    """
    def __init__(self, name, lives=1):
        self._name = name
        self.lives = int(lives)

    def name(self):
        return self._name

    def set_name(self, new_name):
        if not new_name:
            raise ValueError("Name cannot be empty")
        self._name = str(new_name).title()

    def info(self):
        """
        Return basic information about player
        """
        if self.lives == 1:
            return f"My name is {self._name}. I have 1 life left."

        return f"My name is {self._name}. I have {self.lives} lives left."

    def __str__(self):
        return self.info()
