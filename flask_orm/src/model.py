from sqlalchemy import Integer, Sequence

from db import db


class RoomModel(db.Model):
    __tablename__ = 'room_table'
    id = db.Column(Integer, Sequence('room_id', start=1, increment=1))
    number = db.Column(db.Integer, primary_key=True, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='available', nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tenants = db.relationship('TenantModel', backref='room')


class TenantModel(db.Model):
    __tablename__ = 'tenant_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    passport_id = db.Column(db.String(10), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    address = db.Column(db.JSON, nullable=False)
    room_number = db.Column(db.Integer, db.ForeignKey('room_table.number'))


stuff_to_room = db.Table('stuff_to_room',
                         db.Column('room_number', db.Integer, db.ForeignKey('room_table.number')),
                         db.Column('stuff_id', db.Integer, db.ForeignKey('stuff_table.id'))
                         )


class StuffModel(db.Model):
    __tablename__ = 'stuff_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    passport_id = db.Column(db.String(10), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    serving = db.relationship('RoomModel', secondary=stuff_to_room, backref=db.backref('rooms'))
