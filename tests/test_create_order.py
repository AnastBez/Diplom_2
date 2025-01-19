from data import IngredientsHush, StatusCodes
from helpers.helpers_login_user import LoginClient
from helpers.helpers_create_user import RequestsUser
from helpers.helpers_order import Orders
import allure


class TestCreateOrder:

    @allure.title('Cоздание заказа для авторизованного пользователя')
    def test_create_order_auth_client(self):
        user_data = LoginClient.register_and_login_client()
        token = (user_data['accessToken'])
        headers = {"authorization": token}
        order = {"ingredients": [IngredientsHush.BUN]}
        response_order = Orders.make_order(payload=order, headers=headers)
        assert (response_order.status_code == StatusCodes.OK and response_order.json()['success']
                and 'owner' in response_order.json()['order'])
        RequestsUser.delete_user(headers)

    @allure.title('Cоздание заказа для неавторизованного пользователя')
    def test_create_order_not_auth_client(self):
        order = {"ingredients": [IngredientsHush.BUN, IngredientsHush.MAIN]}
        response_order = Orders.make_order(payload=order, headers={})
        assert response_order.status_code == StatusCodes.OK and 'owner' not in response_order.json()['order']

    @allure.title('Cоздание заказа с ингредиентами')
    def test_create_order_with_ingredients(self):
        user_data = LoginClient.register_and_login_client()
        token = (user_data['accessToken'])
        headers = {"authorization": token}
        order = {"ingredients": [IngredientsHush.BUN, IngredientsHush.MAIN, IngredientsHush.SAUCE]}
        response_order = Orders.make_order(payload=order, headers=headers)
        assert response_order.status_code == StatusCodes.OK and response_order.json()['success']
        RequestsUser.delete_user(headers)

    @allure.title('Cоздание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        user_data = LoginClient.register_and_login_client()
        token = (user_data['accessToken'])
        headers = {"authorization": token}
        order = {"ingredients": ""}
        response_order = Orders.make_order(payload=order, headers=headers)
        assert response_order.status_code == StatusCodes.BAD_REQUEST and not response_order.json()['success']
        RequestsUser.delete_user(headers)

    @allure.title('Cоздание заказа с некорректным хешем ингредиента')
    def test_create_order_not_correct_ingredient_hash(self):
        user_data = LoginClient.register_and_login_client()
        token = (user_data['accessToken'])
        headers = {"authorization": token}
        order = {"ingredients": ["6"]}
        response_order = Orders.make_order(payload=order, headers=headers)
        assert response_order.status_code == StatusCodes.ERROR_500
        RequestsUser.delete_user(headers)
