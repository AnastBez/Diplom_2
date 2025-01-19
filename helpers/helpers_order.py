import requests
from data import Endpoint
import allure


class Orders:
    @staticmethod
    @allure.step("Создание заказа")
    def make_order(payload, headers):
        request_url = Endpoint.CREATE_ORDER
        return requests.post(f'{request_url}', json=payload,  headers=headers)
