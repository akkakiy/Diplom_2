import allure
import pytest
import requests

from data import Endpoints, Massage
from help import User


@allure.suite('Проверки изменения данных пользователя')
class TestUpdateUser:
    @allure.title('Проверка изменения данных при авторизации')
    @pytest.mark.parametrize('field_to_update', ['email', 'password', 'name'])
    def test_update_user_with_login(self, user_full_cycle, field_to_update):
        get_token = user_full_cycle[1].json()['accessToken']
        response = requests.patch(f'{Endpoints.USER_UPDATE_URL}',
                                  data=User.valid_user,
                                  headers={'Authorization': f'{get_token}'})
        assert response.status_code == 200 and response.json()['success'] is True

    @allure.title('Проверка изменения данных без авторизации')
    @pytest.mark.parametrize('field_to_update', ['email', 'password', 'name'])
    def test_update_user_without_login(self, user_full_cycle, field_to_update):
        get_token = None
        response = requests.patch(f'{Endpoints.USER_UPDATE_URL}',
                                  data=User.valid_user,
                                  headers={'Authorization': f'{get_token}'})
        assert response.status_code == 401
        assert response.json()['success'] is False
        assert response.json()['message'] == Massage.ERROR_MASSAGE_NOT_AUTHORIZE
