from model import StuffModel

records = [
    StuffModel(name='Zina', passport_id='AK123432', position='waiter', salary='1000'),
    StuffModel(name='Gena', passport_id='BF555434', position='cleaning', salary='1200')
]


def db_init_stuff(db):
    if not StuffModel.query.all():  # if not empty add stubs
        for record in records:
            db.session.add(record)

    return db.session
