from model import TenantModel

records = [
]


def db_init_room(db):
    if not TenantModel.query.all():  # if not empty add stubs
        for record in records:
            db.session.add(record)

    return db.session
