from data import Api
from data import OrderData
import requests
import allure


class TestOrdersList:

    @allure.title('Проверка получения списка заказов: GET /api/v1/orders')
    def test_get_orders_list_success(self):
        response = requests.get(f'{Api.URL}{Api.GET_ORDERS_LIST_API}')
        assert response.status_code == 200 and response.json()[OrderData.success_response_order] != ''

# pytest tests/test_orders_list.py
