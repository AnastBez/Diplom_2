from data import StatusCodes
from data import Endpoint
import requests
from helpers.helpers_login_user import LoginClient
from helpers.helpers_create_user import RequestsUser
import allure


class TestUpdateUser:

    @allure.title('Обновление данных авторизованного пользователя')
    def test_update_auth_user_name(self):
        user_data = LoginClient.register_and_login_client()
        token = (user_data['accessToken'])
        updated_name = user_data["user"]["name"] + "abc"
        updated_data = {"email": user_data["user"]["email"], "name": updated_name}
        response_update = requests.patch(Endpoint.UPD_USER_INFO, json=updated_data, headers={"authorization": token})
        assert response_update.status_code == StatusCodes.OK and response_update.json().get("success")
        RequestsUser.delete_user(headers={"authorization": token})

    @allure.title('Обновление данных неавторизованного пользователя')
    def test_update_not_auth_user_email(self):
        user_data = LoginClient.register_and_login_client()
        updated_email = user_data["user"]["email"] + "qazwsxc"
        updated_data = {"name": user_data["user"]["name"], "email": updated_email}
        response_update = requests.patch(Endpoint.UPD_USER_INFO, json=updated_data)
        assert response_update.status_code == StatusCodes.UNAUTHORIZED and not response_update.json().get("success")
        RequestsUser.delete_user({"authorization": user_data['accessToken']})
