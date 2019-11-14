import uuid


class Restaurant:
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars
        self.id = str(uuid.uuid4())


class Table:
    def __init__(self, number, guests_count):
        self.number = number
        self.guest_count = guests_count
        self.id = str(uuid.uuid4())


class City:
    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())
