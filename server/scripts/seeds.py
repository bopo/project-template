import random

from django_seed import Seed
from service.backend.models import Country
from service.discover.models import Location


'''
{{ object.city }}
{{ object.address }}
{{ object.zip_code }}
{{ object.latitude }}
{{ object.longitude }}
'''
def run():
    seeder = Seed.seeder()

    seeder.add_entity(Location, 1000, {
        'city': lambda x: seeder.faker.city(),
        'address': lambda x: seeder.faker.address(),
        'zip_code': lambda x: seeder.faker.zipcode(),
        'latitude': lambda x: seeder.faker.latitude(),
        'longitude': lambda x: seeder.faker.longitude(),
    })

    seeder.execute()

# def run():
#     seeder = Seed.seeder()

#     seeder.add_entity(Country, 10000, {
#         'name': lambda x: seeder.faker.country(),
#     })

#     seeder.execute()
