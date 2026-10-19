import pytest
import requests
import allure

from utils import URL, make_body, delete_obj


@pytest.fixture(scope='session')
def session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def func():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def get_id_created():
    with allure.step('Creating an object and getting an id of it'):
        headers = {'Content-Type': 'application/json'}
        body = make_body()
        response = requests.post(f'{URL}/object', headers=headers, json=body)
        yield response.json()["id"]
    with allure.step(f'Deleting the object with id: {response.json()["id"]}'):
        delete_obj(response.json()["id"])
