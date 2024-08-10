import allure
import requests

from data import Endpoints, Massage
from help import RealUser, GetIngredients


@allure.suite('Проверки создания заказа')
class TestCreateOrder:
    @allure.title('Тест создания заказа с авторизацией и ингредиентами')
    def test_create_order_with_login_and_ingredients(self):
        login_user = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=RealUser.real_user)
        token = login_user.json()['accessToken']
        data_ingredients = GetIngredients.get_ingredients()
        order = requests.post(f'{Endpoints.CREATE_ORDER_URL}', data={'ingredients': data_ingredients},
                              headers={'Authorization': f'{token}'})
        assert order.status_code == 200 and order.json()['success'] is True

    @allure.title('Тест создания заказа без авторизации, но с ингредиентами')
    def test_create_order_without_login_and_ingredients(self):
        token = ''
        data_ingredients = GetIngredients.get_ingredients()
        order = requests.post(f'{Endpoints.CREATE_ORDER_URL}', data={'ingredients': data_ingredients},
                              headers={'Authorization': f'{token}'})
        assert order.status_code == 200 and order.json()['success'] is True

    @allure.title('Тест создания заказа с авторизацией без ингредиентов')
    def test_create_order_with_login_without_ingredients(self):
        login_user = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=RealUser.real_user)
        token = login_user.json()['accessToken']
        data_ingredients = ''
        order = requests.post(f'{Endpoints.CREATE_ORDER_URL}', data={'ingredients': data_ingredients},
                              headers={'Authorization': f'{token}'})
        assert order.status_code == 400 and order.json()['message'] == Massage.ERROR_MESSAGE_INGREDIENT

    @allure.title('Тест создания заказа с авторизацией и некорректными ингредиентами')
    def test_create_order_with_login_and_incorrect_ingredients(self):
        login_user = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=RealUser.real_user)
        token = login_user.json()['accessToken']
        data_ingredients = {'ingredients': ['1', '2']}
        order = requests.post(f'{Endpoints.CREATE_ORDER_URL}', data={'ingredients': data_ingredients},
                              headers={'Authorization': f'{token}'})
        assert order.status_code == 500
