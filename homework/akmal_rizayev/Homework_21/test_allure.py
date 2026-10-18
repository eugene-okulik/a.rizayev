import pytest
import requests
import allure

from utils import URL, get_one_obj, delete_obj, make_body


@allure.feature('GET requests')
@allure.story('Get one object')
def test_get_one_obj(get_id_created, session, func):
    with allure.step(f'Getting an object with id {get_id_created}'):
        response = requests.get(f'{URL}/object/{get_id_created}')
    with allure.step('Checking if response status code is 200'):
        assert response.status_code == 200
    with allure.step('Checking if the object id is equal to the created one'):
        assert response.json()['id'] == get_id_created


@allure.feature('GET requests')
@allure.story('Get all objects')
@pytest.mark.critical
def test_get_all_obj(get_id_created, session, func):
    with allure.step('Getting all the objects'):
        response = requests.get(f'{URL}/object')
    with allure.step('Checking if response status code is 200'):
        assert response.status_code == 200
    with allure.step(f'Checking if a created object with id: {get_id_created} is in the response list'):
        assert get_id_created in map(lambda x: x["id"], response.json()["data"])


@allure.feature('POST requests')
@allure.story('Add one object')
@pytest.mark.parametrize('body', [make_body() for _ in range(3)])
def test_add_obj(body, session, func):
    with allure.step(f'Creating object with body: {body}'):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f'{URL}/object', headers=headers, json=body)
    with allure.step('Checking if response status code is 200'):
        assert response.status_code == 200
    with allure.step(f'Deleting the object with id {response.json()["id"]}'):
        delete_obj(response.json()["id"])


@allure.feature('PUT requests')
@allure.story('Change one object')
@pytest.mark.medium
def test_put_obj(get_id_created, session, func):
    body = {"name": "EditedName", "data": {"prop3": "value1", "prop4": "value2"}}
    with allure.step(f'Changing the object to {str(body)}'):
        headers = {'Content-Type': 'application/json'}
        response = requests.put(f'{URL}/object/{get_id_created}', headers=headers, json=body)
    with allure.step('Checking if response status code is 200'):
        assert response.status_code == 200
    with allure.step(f'Checking if name is changed to {body["name"]}'):
        assert response.json()['name'] == 'EditedName'
    with allure.step(f'Checking if data is changed to {body["data"]}'):
        assert response.json()['data'] == body["data"]


@allure.feature('PATCH requests')
@allure.story('Change certain properties of an object')
def test_patch_obj(get_id_created, session, func):
    body = {"name": "NewEditedName"}
    with allure.step(f'Changing only the name of the object to {body["name"]}'):
        headers = {'Content-Type': 'application/json'}
        response = requests.patch(f'{URL}/object/{get_id_created}', headers=headers, json=body)
    with allure.step('Checking if response status code is 200'):
        assert response.status_code == 200
    with allure.step(f'Checking if name of the object is changed to {body["name"]}'):
        assert response.json()['name'] == body["name"]
    with allure.step('Checking if the address of the object still exists'):
        assert response.json()["data"]["address"] is not None


@allure.feature('DELETE requests')
@allure.story('Delete one object')
def test_delete_obj(get_id_created, session, func):
    with allure.step(f'Deleting the object with id: {get_id_created}'):
        headers = {'Content-Type': 'application/json'}
        response = requests.delete(f'{URL}/object/{get_id_created}', headers=headers)
    with allure.step('Checking if response status code is 200'):
        assert response.status_code == 200
    with allure.step(f'Checking if GET {URL}/object/{get_id_created} responds with 404'):
        assert get_one_obj(get_id_created).status_code == 404
