import allure
import pytest
import requests

from data import Endpoints, Massage
from help import User, RegisterLoginDeleteUser


@allure.suite('Проверки создания пользователя')
class TestCreateUser:
    @allure.title('Тест создания пользователя')
    def test_create_user(self, user_full_cycle):
        assert user_full_cycle[0].status_code == 200 and user_full_cycle[0].json()['success'] is True

    @allure.title('Тест создания пользователя без заполнения одного или всех обязательных полей')
    @pytest.mark.parametrize('user', [User.invalid_user_without_email,
                                      User.invalid_user_without_password,
                                      User.invalid_user_without_name,
                                      User.invalid_user_without_data])
    def test_create_user_without_fields(self, user, user_full_cycle):
        response = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=user)
        assert response.status_code == 403 and response.json()['message'] == Massage.ERROR_MASSAGE_CREATE_DATA_INCORRECT

    @allure.title('Тест создания существующего пользователя')
    def test_create_duplicate_user(self, user_full_cycle):
        response = RegisterLoginDeleteUser.register_user()
        assert response['status_code'] == 403
        assert response['response_text'] == Massage.ERROR_MASSAGE_CREATE_DUPLICATE
