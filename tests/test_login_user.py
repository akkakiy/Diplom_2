import allure
import requests

from data import Endpoints, Massage
from help import LaiUser, RealUser


@allure.suite('Проверки авторизации пользователя')
class TestLoginUser:
    @allure.title('Проверка авторизации пользователя')
    def test_login_real_user(self):
        response = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=RealUser.real_user)
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка авторизации несуществующего пользователя')
    def test_login_lai_user(self):
        response = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=LaiUser.lai_user)
        assert (response.status_code == 401 and
                response.json()['message'] == Massage.ERROR_MASSAGE_AUTHORIZE_AND_LOGIN_INCORRECT)
