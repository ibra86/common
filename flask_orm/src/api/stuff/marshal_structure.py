from flask_restful import fields

fields_structure = {'id': fields.Integer,
                    'name': fields.String,
                    'passport_id': fields.String,
                    'position': fields.Integer,
                    'salary': fields.Integer,
                    }
