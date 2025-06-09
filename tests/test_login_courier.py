from data import Api
import requests
from data import Response
import allure


class TestLoginCourier:
    @allure.title('Проверка авторизации курьера: POST /api/v1/courier/login')
    @allure.step('Проверить, что курьер авторизировался: POST /api/v1/courier')
    def test_login_courier_success(self, login_courier):
        response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=login_courier[1])
        assert response.status_code == 200 and 'id' in response.json()

    @allure.step('Проверить появление ошибки при авторизации несуществующего курьера: POST /api/v1/courier/login')
    def test_login_non_existent_courier_error(self, create_data_courier):
        response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=create_data_courier)
        assert response.status_code == 404 and response.json() == Response.NOT_FOUND_COURIER

    @allure.step('Проверить появление ошибки при авторизации без логина: POST /api/v1/courier/login')
    def test_login_courier_without_login_error(self, login_courier):
        login_courier_body = {'login': '', 'password': login_courier[2]}
        response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=login_courier_body)
        assert response.status_code == 400 and response.json() == Response.BED_REQ_LOGIN_COURIER

    @allure.step('Проверить появление ошибки при авторизации без пароля: POST /api/v1/courier/login')
    def test_login_courier_without_password_error(self, login_courier):
        login_courier_body = {'login': login_courier[3], 'password': ''}
        response = requests.post(f'{Api.URL}{Api.LOGIN_COURIER_API}', json=login_courier_body)
        assert response.status_code == 400 and response.json() == Response.BED_REQ_LOGIN_COURIER

# pytest tests/test_login_courier.py
