from model import Room

DB = dict.fromkeys(['room', 'tenants', 'stuff'], [])

# DB['room'] = [{'number': 101,
#                'level': 3,
#                'status': 'available',
#                'price': 1000}]

DB['room'] = [Room(101, 3, 'available', 1000),
              Room(1, 2, 'closed', 300)]
