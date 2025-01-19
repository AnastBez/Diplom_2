import pytest
from data import StatusCodes
from helpers.helpers_create_user import generate_random_user, RequestsUser
from helpers.helpers_login_user import LoginClient

import allure


class TestLoginUser:
    @pytest.mark.parametrize(
        'email, password, name',
        [
            (generate_random_user()['email'],
             generate_random_user()['password'],
             generate_random_user()['name']
             )
        ]
    )
    @allure.title('Авторизация существующего пользователя')
    def test_login_exist_user(self, email, password, name):
        RequestsUser.create_user({'email': email, 'password': password, 'name': name})
        payload = {'email': email, 'password': password}
        response = LoginClient.request_on_login_user(payload)
        assert (response.status_code == StatusCodes.OK and 'accessToken' in response.json())
        RequestsUser.delete_user({"authorization": response.json()['accessToken']})

    @allure.title('Авторизация пользователя с некорректным логином и паролем')
    def test_login_uncorrected_user(self):
        payload = {'email': 'knfknfkv@ya.ru', 'password': 'pass'}
        response = LoginClient.request_on_login_user(payload)
        assert (response.status_code == StatusCodes.UNAUTHORIZED and not response.json()['success'])
