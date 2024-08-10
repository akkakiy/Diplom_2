class Endpoints:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'

    INGREDIENTS_URL = f'{MAIN_URL}api/ingredients'

    CREATE_ORDER_URL = f'{MAIN_URL}api/orders'

    PASS_RESET_URL = f'{MAIN_URL}password-reset'

    RESET_PASSWORD_URL = f'{MAIN_URL}api/password-reset'

    USER_REGISTER_URL = f'{MAIN_URL}api/auth/register'

    USER_LOGIN_URL = f'{MAIN_URL}api/auth/login'

    USER_LOGOUT_URL = f'{MAIN_URL}api/auth/logout'

    TOKEN_URL = f'{MAIN_URL}api/auth/token'

    USER_INFO_URL = f'{MAIN_URL}api/auth/user'

    USER_UPDATE_URL = f'{MAIN_URL}api/auth/user'

    USER_DELETE_URL = f'{MAIN_URL}api/auth/user'

    ALL_ORDERS_URL = f'{MAIN_URL}api/orders/all'

    USER_ORDER_INFO_URL = f'{MAIN_URL}api/orders'


class Massage:
    ERROR_MESSAGE_INGREDIENT = 'Ingredient ids must be provided'
    ERROR_MASSAGE_CREATE_DUPLICATE = '{"success":false,"message":"User already exists"}'
    ERROR_MASSAGE_CREATE_DATA_INCORRECT = 'Email, password and name are required fields'
    ERROR_MASSAGE_AUTHORIZE_AND_LOGIN_INCORRECT = 'email or password are incorrect'
    ERROR_MASSAGE_EMAIL_EXIST = 'User with such email already exists'
    ERROR_MASSAGE_NOT_AUTHORIZE = 'You should be authorised'
