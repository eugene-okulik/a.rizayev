import requests

URL = 'http://objapi.course.qa-practice.com'


def get_all_obj():
    response = requests.get(f'{URL}/object')
    assert response.status_code == 200
    return response.json()


def get_one_obj(_id):
    response = requests.get(f'{URL}/object/{_id}')
    if response.status_code == 200:
        assert response.json()['id'] == _id
    return response


def add_obj():
    headers = {'Content-Type': 'application/json'}
    body = {"name": "FirstName", "data": {"prop1": "value1", "prop2": "value2"}}
    response = requests.post(f'{URL}/object', headers=headers, json=body)
    assert response.status_code == 200
    return response.json()['id']


def put_obj():
    _id = add_obj()
    headers = {'Content-Type': 'application/json'}
    body = {"name": "EditedName", "data": {"prop3": "value1", "prop4": "value2"}}
    response = requests.put(f'{URL}/object/{_id}', headers=headers, json=body)
    assert response.status_code == 200
    assert response.json()['name'] == 'EditedName'
    assert response.json()['data'] == {"prop3": "value1", "prop4": "value2"}
    return response.json()


def patch_obj():
    _id = add_obj()
    headers = {'Content-Type': 'application/json'}
    body = {"name": "NewEditedName"}
    response = requests.patch(f'{URL}/object/{_id}', headers=headers, json=body)
    assert response.status_code == 200
    assert response.json()['name'] == 'NewEditedName'
    return response.json()


def delete_obj():
    _id = add_obj()
    headers = {'Content-Type': 'application/json'}
    body = {}
    response = requests.delete(f'{URL}/object/{_id}', headers=headers, json=body)
    assert get_one_obj(_id).status_code == 404
    return response.status_code


print(get_all_obj())
print(get_one_obj(1).json())
print(add_obj())
print(put_obj())
print(patch_obj())
print(delete_obj())
