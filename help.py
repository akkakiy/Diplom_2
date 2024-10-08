import requests

from faker import Faker
from data import Endpoints


class CreateRandomUser:
    @staticmethod
    def create_random_user():       # создание пользователя
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': faker.password(),
            'name': faker.name()
        }
        return user

    @staticmethod
    def create_random_user_without_email():         # создание пользователя без email
        faker = Faker('ru_RU')
        user = {
            'email': '',
            'password': faker.password(),
            'name': faker.name()
        }
        return user

    @staticmethod
    def create_random_user_without_password():      # создание пользователя без пароля
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': '',
            'name': faker.name()
        }
        return user

    @staticmethod
    def create_random_user_without_name():       # создание пользователя без имени
        faker = Faker('ru_RU')
        user = {
            'email': faker.email(),
            'password': faker.password(),
            'name': ''
        }
        return user

    @staticmethod
    def create_random_user_without_data():       # создание пользователя без данных
        user = {
            'email': '',
            'password': '',
            'name': ''
        }
        return user


class User:                                     # создание пользователя
    valid_user = CreateRandomUser.create_random_user()
    invalid_user_without_email = CreateRandomUser.create_random_user_without_email()
    invalid_user_without_password = CreateRandomUser.create_random_user_without_password()
    invalid_user_without_name = CreateRandomUser.create_random_user_without_name()
    invalid_user_without_data = CreateRandomUser.create_random_user_without_data()


class RegisterLoginDeleteUser:
    @staticmethod
    def register_user():                        # регистрация пользователя
        valid_user = User.valid_user
        response = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=valid_user)
        return {'response_text': response.text, 'status_code': response.status_code, 'data_user': valid_user}


class LaiUser:                                  # несуществующий пользователь
    lai_user = {
        'email': 'akkakiy@gmailcom',
        'password': 'Zaq12wsxcde34rfv',
        'name': 'Maximka'
    }


class GetIngredients:                           # получение списка ингредиентов
    @staticmethod
    def get_ingredients(limit=4):
        response = requests.get(f'{Endpoints.INGREDIENTS_URL}')
        ingredients = response.json()['data']
        ingredients_list = []
        for i in ingredients:
            ingredients_list.append(i['_id'])
            if len(ingredients_list) == limit:
                break
        return ingredients_list
