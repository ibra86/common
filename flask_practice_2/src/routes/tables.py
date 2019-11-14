import json

from flask import Blueprint, Response, request
from src.insrastructure import DB
from src.model import Table

tables = Blueprint('tables', __name__)


@tables.route('/tables', methods=['GET'])
def get_tables():
    result = [{'number': table.number, 'guest_count': table.guest_count} for table in DB['table']]
    data = json.dumps(result)
    return Response(data, status=200)


@tables.route('/tables', methods=['POST'])
def restaurants_create():
    data = request.json
    DB['table'].append(Table(data['number'], data['guest_count']))
    return Response(status=200)
