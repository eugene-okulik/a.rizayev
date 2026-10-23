import allure
import requests

from test_api_arizayev.endpoints.Endpoint import Endpoint


class GetObject(Endpoint):
@allure.feature('GET requests')
@allure.story('Get one object')
def test_get_one_obj(get_id_created, session, func):
    with allure.step(f'Getting an object with id {get_id_created}'):
        response = requests.get(f'{URL}/object/{get_id_created}')
    with allure.step('Checking if response status code is 200'):
        assert response.status_code == 200
    with allure.step('Checking if the object id is equal to the created one'):
        assert response.json()['id'] == get_id_created