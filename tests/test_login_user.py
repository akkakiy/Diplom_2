import allure
import requests

from data import Endpoints, Massage
from help import LaiUser


@allure.suite('Проверки авторизации пользователя')
class TestLoginUser:
    @allure.title('Проверка авторизации пользователя')
    def test_login_real_user(self, user_registration_and_login):
        token = user_registration_and_login[1].json()['accessToken']
        assert user_registration_and_login[1].status_code == 200
        assert user_registration_and_login[1].json()['success'] is True
        requests.delete(f'{Endpoints.USER_DELETE_URL}', headers={'Authorization': f'{token}'})

    @allure.title('Проверка авторизации несуществующего пользователя')
    def test_login_lai_user(self):
        response = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=LaiUser.lai_user)
        assert response.status_code == 401
        assert response.json()['message'] == Massage.ERROR_MASSAGE_AUTHORIZE_AND_LOGIN_INCORRECT
