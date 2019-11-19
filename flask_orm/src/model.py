from db import db


class RoomModel(db.Model):
    __tablename__ = 'room_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='available', nullable=False)
    price = db.Column(db.Integer, nullable=False)

# class Room:
#     def __init__(self, number, level, status, price):
#         self.number = number
#         self.level = level
#         self.status = status
#         self.price = price


# class Tenant:
#     def __init__(self, name, passport_id, age, sex, address, room_number):
#         self.name = name
#         self.passport_id = passport_id
#         self.age = age
#         self.sex = sex
#         self.address = address
#         self.room_number = room_number
#
#
# class Stuff:
#     def __init__(self, name, passport_id, position, salary):
#         self.name = name
#         self.passport_id = passport_id
#         self.position = position
#         self.salary = salary
