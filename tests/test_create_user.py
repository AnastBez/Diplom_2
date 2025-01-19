from helpers.helpers_create_user import *
from data import StatusCodes
import pytest
import allure


class TestCreateUser:
    @allure.title('Регистрация уникального пользователя')
    def test_create_original_user(self):
        create_user_data = generate_random_user()
        response = RequestsUser.create_user(create_user_data)
        assert response.status_code == StatusCodes.OK and response.json()['success']
        RequestsUser.delete_user({"authorization": response.json()['accessToken']})

    @allure.title('Регистрация существующего пользователя')
    def test_create_exist_user(self):
        create_user_data_1 = generate_random_user()
        response_1 = RequestsUser.create_user(create_user_data_1)
        response_2 = RequestsUser.create_user(create_user_data_1)
        assert response_2.status_code == StatusCodes.FORBIDDEN and not response_2.json()['success']
        RequestsUser.delete_user({"authorization": response_1.json()['accessToken']})

    @pytest.mark.parametrize(
        'email, password, name',
        [
            ('',
             generate_random_user()['password'],
             generate_random_user()['name']),

            (generate_random_user()['email'],
             '',
             generate_random_user()['name']),

            (generate_random_user()['email'],
             generate_random_user()['password'],
             '',)

        ]
    )
    @allure.title('Регистрация пользователя без обязательного поля')
    def test_create_required_fields(self, email, password, name):
        response = RequestsUser.create_user({'email': email, 'password': password, 'name': name})
        assert response.status_code == StatusCodes.FORBIDDEN and not response.json()['success']
