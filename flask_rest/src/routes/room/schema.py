from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema

room_schema = {'number': 'integer',
               'level': 'integer',
               'status': 'string',
               'price': 'number'}


class RoomInputs(Inputs):
    json = [JsonSchema(schema=room_schema)]


def validate_room(request):
    inputs = RoomInputs(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors
