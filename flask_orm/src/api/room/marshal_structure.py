from flask_restful import fields

fields_structure = {'id': fields.Integer,
                    'number': fields.Integer,
                    'level': fields.Integer,
                    'status': fields.String,
                    'price': fields.Float,
                    }
