from db import db
from model import RoomModel

records = [
    RoomModel(number=101, level=1, price=1000),
    RoomModel(number=502, level=5, status='closed', price=100),
    RoomModel(number=703, level=7, status='closed', price=500),
    RoomModel(number=612, level=6, price=300),
    RoomModel(number=150, level=1, price=100),
]


def db_init_room(db):
    for record in records:
        db.session.add(record)

    return db.session
