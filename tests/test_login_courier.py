from data import Api
import requests
from data import Response
import allure


class TestLoginCourier:
    @allure.title('Проверка успешной авторизации: POST /api/v1/courier/login')
    def test_login_courier_success(self, login_courier):
        assert login_courier[0].status_code == 200 and 'id' in login_courier[0].json()

    @allure.title('Проверка появления ошибки при авторизации несуществующего курьера: POST /api/v1/courier/login')
    def test_login_non_existent_courier_error(self, create_data_courier):
        response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=create_data_courier)
        assert response.status_code == 404 and response.json() == Response.NOT_FOUND_COURIER

    @allure.title('Проверка появления ошибки при авторизации без логина: POST /api/v1/courier/login')
    def test_login_courier_without_login_error(self, registration_courier):
        login_courier_body = {'login': '', 'password': registration_courier[1]}
        response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=login_courier_body)
        assert response.status_code == 400 and response.json() == Response.BED_REQ_LOGIN_COURIER

    @allure.title('Проверка появления ошибки при авторизации без пароля: POST /api/v1/courier/login')
    def test_login_courier_without_password_error(self, registration_courier):
        login_courier_body = {'login': registration_courier[2], 'password': ''}
        response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=login_courier_body)
        assert response.status_code == 400 and response.json() == Response.BED_REQ_LOGIN_COURIER

# pytest tests/test_login_courier.py
