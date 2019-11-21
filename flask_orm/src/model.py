from db import db


class RoomModel(db.Model):
    __tablename__ = 'room_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.Integer, unique=True, nullable=False)
    level = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), default='available', nullable=False)
    price = db.Column(db.Integer, nullable=False)


class TenantModel(db.Model):
    __tablename__ = 'tenant_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    passport_id = db.Column(db.String(10), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    address = db.Column(db.JSON(50), nullable=False)
    room_number = db.Column(db.String(50), nullable=False)


class StuffModel(db.Model):
    __tablename__ = 'stuff_table'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    passport_id = db.Column(db.String(10), unique=True, nullable=False)
    position = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer, nullable=False)
