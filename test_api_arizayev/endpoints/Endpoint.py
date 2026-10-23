import allure
from faker import Faker
import requests

URL = 'http://objapi.course.qa-practice.com'

fake = Faker()

class Endpoint:

    def __init__(self):
        self.url = 'http://objapi.course.qa-practice.com'
        self.headers = None
        self.body = None
        self.response = None

    @allure.step('Checking if response status code is {stat}')
    def if_status_equals(self, stat):
        assert self.response.status == stat

    def get_id_created(self):
        self.headers = {'Content-Type': 'application/json'}
        self.body = self.make_body()
        response = requests.post(f'{URL}/object', headers=self.headers, json=self.body)
        return response.json()["id"]

    def delete_id_created(self):


    @staticmethod
    def make_body():
        return {
            "name": fake.name(),
            "data": {
                "birth_date": str(fake.date_of_birth()),
                "address": fake.address(),
            },
        }