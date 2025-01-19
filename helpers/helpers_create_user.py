import requests
import random
from data import Endpoint
import string
import allure


def generate_random_user():
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)) + "@yandex.ru"
    password = ''.join(random.choices(string.ascii_lowercase,  k=10))
    name = ''.join(random.choices(string.ascii_lowercase,  k=10))

    return {"email": email, "password": password, "name": name}


class RequestsUser:

    @staticmethod
    @allure.step("Регистрация юзера")
    def create_user(payload: dict):
        request_url = Endpoint.CREATE_USER
        return requests.post(f'{request_url}', json=payload)

    @staticmethod
    @allure.step("Удаление юзера")
    def delete_user(headers: dict):
        request_url = Endpoint.DELETE_USER
        return requests.delete(f'{request_url}', headers=headers)
