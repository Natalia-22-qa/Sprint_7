import pytest
from data import Api
import requests
from data import Response
from data import Courier
import allure


class TestCreateCourier:
    @allure.title('Проверка создания курьера: POST /api/v1/courier')
    @allure.step('Проверить, что новый курьер регистрируется в системе')
    def test_create_courier_success(self, registration_courier):
        response = requests.post(f'{Api.URL}{Api.CREATE_COURIER_API}', json=registration_courier)
        assert response.status_code == 201 and response.json() == Response.SUCCESS_CREATE_COURIER

    @allure.step('Проверить появление ошибки при создании одинаковых курьеров: POST /api/v1/courier')
    def test_create_courier_clone_error(self, login_courier):
        response = requests.post(f'{Api.URL}{Api.CREATE_COURIER_API}', json=login_courier[0])
        assert response.status_code == 409 and response.json() == Response.CONFLICT_CREATE_COURIER

    @allure.step('Проверить появление ошибки при отсутствии обязательного поля: POST /api/v1/courier')
    @pytest.mark.parametrize('data', Courier.reg_data)
    def test_create_courier_without_required_field_error(self, data):
        response = requests.post(f'{Api.URL}{Api.CREATE_COURIER_API}', json=Courier.reg_data)
        assert response.status_code == 400 and response.json() == Response.BED_REQ_CREATE_COURIER

# pytest tests/test_create_courier.py
