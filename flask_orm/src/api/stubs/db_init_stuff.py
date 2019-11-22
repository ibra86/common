from model import StuffModel

records = [
]


def db_init_room(db):
    if not StuffModel.query.all():  # if not empty add stubs
        for record in records:
            db.session.add(record)

    return db.session
