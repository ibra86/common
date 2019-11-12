from flask_restful import Resource, fields, marshal_with

resource_fields = {'number': fields.Integer,
                   'level': fields.Integer,
                   'status': fields.String,
                   'price': fields.Float}


# class TodoDao(object):
#     def __init__(self, todo_id, task):
#         self.todo_id = todo_id
#         self.task = task
#         # This field will not be sent in the response
#         self.status = 'active'
#
# class Todo(Resource):
#     @marshal_with(resource_fields)
#     def get(self, **kwargs):
#         return TodoDao(todo_id='my_todo', task='Remember the milk')

class RoomView(Resource):
    def get(self, number):
        if number:
            pass

    def post(self, number):
        pass

    def delete(self, number):
        pass
