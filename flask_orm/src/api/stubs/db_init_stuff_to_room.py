from api.stubs import db_init_stuff, db_init_room

from itertools import product


def db_init_stuff_to_room(db):
    s_records = db_init_stuff.records
    r_records = db_init_room.records

    pairs = product(s_records, r_records)

    for s, r in pairs:
        s.serving.append(r)
        db.session.add(s)
    return db.session
