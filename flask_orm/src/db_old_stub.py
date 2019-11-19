from model import Room, Stuff, Tenant

DB = dict.fromkeys(['room', 'tenant', 'stuff'], [])

DB['room'] = [Room(101, 3, 'available', 1000),
              Room(1, 2, 'closed', 300)]
DB['tenant'] = [Tenant('Joe', 'FE156847', 73, 'M', {'city': 'Frankfurt', 'street': 'Williams str., 2'}, 54)]
DB['stuff'] = [Stuff('Ann', 'MK456785', 'waiter', 4000)]
