import requests
from data import Endpoint
from helpers.helpers_create_user import generate_random_user, RequestsUser
import allure


class LoginClient:
    @staticmethod
    @allure.step("Авторизация клиента")
    def request_on_login_user(payload: dict):
        request_url = Endpoint.LOGIN_USER
        return requests.post(f'{request_url}', json=payload)

    @staticmethod
    @allure.step("Регистрация и авторизация клиента")
    def register_and_login_client():
        payload = generate_random_user()
        RequestsUser.create_user(payload)
        login = LoginClient.request_on_login_user({'email': payload['email'], 'password': payload['password']})
        return login.json()
