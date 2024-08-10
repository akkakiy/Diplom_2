import pytest
import requests

import help
from data import Endpoints
from help import User


@pytest.fixture
def user_full_cycle():       # фикстура для создания, авторизации и удаления пользователя
    created_user = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=User.valid_user)
    login_user = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=User.valid_user)
    yield created_user, login_user
    requests.delete(f'{Endpoints.USER_DELETE_URL}', data=User.valid_user)


@pytest.fixture
def user_registration_and_login():       # фикстура для регистрации и авторизации пользователя
    created_user = requests.post(f'{Endpoints.USER_REGISTER_URL}', data=User.valid_user)
    login_user = requests.post(f'{Endpoints.USER_LOGIN_URL}', data=User.valid_user)
    yield created_user, login_user


@pytest.fixture
def valid_ingredients():       # фикстура для получения списка ингредиентов
    return help.GetIngredients()
