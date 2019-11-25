from model import TenantModel

records = [
    TenantModel(name='Joe', passport_id='FD242323', age=21, sex='M', address={"street": "Main St.", "zip": 12345},
                room_number=101),
    TenantModel(name='Jude', passport_id='RE876987', age=43, sex='F', address={"street": "Linkoln St.", "zip": 12541},
                room_number=101),
]


def db_init_tenant(db):
    if not TenantModel.query.all():  # if not empty add stubs
        for record in records:
            db.session.add(record)

    return db.session
