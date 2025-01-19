from data import IngredientsHush, StatusCodes
from helpers.helpers_login_user import LoginClient
from helpers.helpers_create_user import RequestsUser
from helpers.helpers_order import Orders
from data import Endpoint
import requests
import allure


class TestOrderList:
    @allure.title('Получение списка заказов авторизованного пользователя')
    def test_get_auth_client_order_list(self):
        user_data = LoginClient.register_and_login_client()
        token = (user_data['accessToken'])
        headers = {"authorization": token}
        order = {"ingredients": [IngredientsHush.BUN]}
        Orders.make_order(payload=order, headers=headers)
        orders = requests.get(Endpoint.ORDER_LIST, headers=headers)
        assert orders.status_code == StatusCodes.OK and orders.json()['success']
        RequestsUser.delete_user(headers)

    @allure.title('Получение списка заказов неавторизованного пользователя')
    def test_get_not_auth_client_order_list(self):
        user_data = LoginClient.register_and_login_client()
        token = (user_data['accessToken'])
        headers = {"authorization": token}
        order = {"ingredients": [IngredientsHush.BUN]}
        Orders.make_order(payload=order, headers=headers)
        orders = requests.get(Endpoint.ORDER_LIST)
        assert orders.status_code == StatusCodes.UNAUTHORIZED and not orders.json()['success']
        RequestsUser.delete_user(headers)
