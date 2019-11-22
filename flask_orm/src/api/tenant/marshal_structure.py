from flask_restful import fields

city_structure = {
    "city": fields.String,
    "street": fields.String
}

fields_structure = {'id': fields.Integer, 'name': fields.String,
                    'passport_id': fields.String,
                    'age': fields.Integer,
                    'sex': fields.String,
                    'address': fields.Nested(city_structure),
                    'room_number': fields.Integer}
