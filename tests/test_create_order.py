import pytest
from data import Api
from data import OrderData
import requests
import allure


class TestCreateOrder:
    @allure.title('Проверка создания заказа с разным цветом самоката: POST /api/v1/orders')
    @pytest.mark.parametrize('color', OrderData.color)
    def test_create_orders_different_colors_success(self, color, cancel_order):
        OrderData.order_body['color'] = color
        response = requests.post(f'{Api.URL}{Api.CREATE_ORDER_API}', json = OrderData.order_body)
        assert response.status_code == 201 and OrderData.success_create_order in response.json()

# pytest tests/test_create_order.py
