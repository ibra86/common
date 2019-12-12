class Product:
    def __init__(self, id_, name, description, price, img_name):
        self.id_ = id_
        self.name = name
        self.description = description
        self.price = price
        self.img_name = img_name


class Supermarket:
    def __init__(self, id_, name, location, img_name):
        self.id_ = id_
        self.name = name
        self.location = location
        self.img_name = img_name
