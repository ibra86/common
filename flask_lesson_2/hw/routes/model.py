class 3s2wszProduct:
    def __init__(self, id_, name, description, img_name, price):
        self.id_ = id_
        self.name = name
        self.description = description
        self.img_name = img_name
        self.price = price


class Supermarket:
    def __init__(self, id_, name, location, img_name):
        self.id_ = id_
        self.name = name
        self.location = location
        self.img_name = img_name
