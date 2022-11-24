class Package:
    def __init__(self, sender, reciever, dimensions, weight):
        self._sender = sender
        self._reciever = reciever
        self._dimensions = dimensions
        self._weight = weight

    def sender(self):
        return self.sender

    def set_sender(self, new_sender):
        if not isinstance(new_sender, str):
            raise ValueError("New sender must be type str")
        self._sender = new_sender

    def reciever(self):
        return self.reciever

    def set_reciever(self, new_reciever):
        if not isinstance(new_reciever, str):
            raise ValueError("New reciever must be type str")
        self._sender = new_reciever

    def dimensions(self):
        return self._dimensions

    def set_dimensions(self, new_dimensions):
        self._dimensions = new_dimensions

    def weight(self):
        return self._weight

    def set_weight(self, new_weight):
        self._weight = new_weight
