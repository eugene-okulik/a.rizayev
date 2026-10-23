from faker import Faker
import requests

URL = 'http://objapi.course.qa-practice.com'

fake = Faker()


def get_one_obj(_id):
    response = requests.get(f'{URL}/object/{_id}')
    return response


def delete_obj(_id):
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(f'{URL}/object/{_id}', headers=headers)
    return response


def make_body():
    return {
        "name": fake.name(),
        "data": {
            "birth_date": str(fake.date_of_birth()),
            "address": fake.address(),
        },
    }
