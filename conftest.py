import pytest
import requests
import data_generation
from data import Api
import json
from data import OrderData

@pytest.fixture
def create_data_courier():
    create_courier_body = data_generation.courier_registration_data()
    login_courier_body = {'login': create_courier_body['login'], 'password': create_courier_body['password']}
    yield login_courier_body

@pytest.fixture
def login_courier():
    create_courier_body = data_generation.courier_registration_data()
    login = create_courier_body['login']
    password = create_courier_body['password']
    login_courier_body = {'login': login, 'password': password}
    requests.post(f'{Api.URL}{Api.CREATE_COURIER_API}', json=create_courier_body)
    login_response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=login_courier_body)
    yield [create_courier_body, login_courier_body, password, login]
    requests.delete(f'{Api.URL}{Api.DELETE_COURIER_API}', params=json.dumps(login_response.json()['id']))

@pytest.fixture
def registration_courier():
    create_courier_body = data_generation.courier_registration_data()
    login_courier_body = {'login': create_courier_body['login'], 'password': create_courier_body['password']}
    yield create_courier_body
    login_response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=login_courier_body)
    requests.delete(f'{Api.URL}{Api.DELETE_COURIER_API}', params=json.dumps(login_response.json()['id']))

@pytest.fixture
def cancel_order():
    response = requests.post(f'{Api.URL}{Api.CREATE_ORDER_API}', json=OrderData.order_body)
    yield
    requests.put(f'{Api.URL}{Api.CANCEL_ORDER_API}', params = json.dumps(response.json()[OrderData.success_create_order]))
