import pytest
import requests

from faker import Faker

URL = 'http://objapi.course.qa-practice.com'

fake = Faker()


def get_one_obj(_id):
    response = requests.get(f'{URL}/object/{_id}')
    return response


def delete_obj(_id):
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(f'{URL}/object/{_id}', headers=headers)
    return response


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
    headers = {'Content-Type': 'application/json'}
    body = {"name": fake.name(), "data": {"birth_date": str(fake.date_of_birth()), "address": str(fake.address())}}
    response = requests.post(f'{URL}/object', headers=headers, json=body)
    yield response.json()["id"]
    delete_obj(response.json()["id"])


def test_get_one_obj(get_id_created, session, func):
    response = requests.get(f'{URL}/object/{get_id_created}')
    assert response.status_code == 200
    assert response.json()['id'] == get_id_created


@pytest.mark.critical
def test_get_all_obj(get_id_created, session, func):
    response = requests.get(f'{URL}/object')
    assert response.status_code == 200
    assert get_id_created in map(lambda x: x["id"], response.json()["data"])


@pytest.mark.parametrize('body', [{"name": fake.name(), "data":
    {"birth_date": str(fake.date_of_birth()), "address": str(fake.address())}} for _ in range(3)])
def test_add_obj(body, session, func):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(f'{URL}/object', headers=headers, json=body)
    assert response.status_code == 200
    delete_obj(response.json()["id"])


@pytest.mark.medium
def test_put_obj(get_id_created, session, func):
    headers = {'Content-Type': 'application/json'}
    body = {"name": "EditedName", "data": {"prop3": "value1", "prop4": "value2"}}
    response = requests.put(f'{URL}/object/{get_id_created}', headers=headers, json=body)
    assert response.status_code == 200
    assert response.json()['name'] == 'EditedName'
    assert response.json()['data'] == {"prop3": "value1", "prop4": "value2"}


def test_patch_obj(get_id_created, session, func):
    headers = {'Content-Type': 'application/json'}
    body = {"name": "NewEditedName"}
    response = requests.patch(f'{URL}/object/{get_id_created}', headers=headers, json=body)
    assert response.status_code == 200
    assert response.json()['name'] == 'NewEditedName'
    assert response.json()["data"]["address"] is not None


def test_delete_obj(get_id_created, session, func):
    headers = {'Content-Type': 'application/json'}
    response = requests.delete(f'{URL}/object/{get_id_created}', headers=headers)
    assert response.status_code == 200
    assert get_one_obj(get_id_created).status_code == 404
