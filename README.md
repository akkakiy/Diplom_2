# Дипломный проект курса "Инженер по тестированию: от новичка до автоматизатора"
## Задания по теме "API-тестирование"

    API-тесты на сервис Stellar Burgers. 
    Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

## Файлы
    - tests/  -  каталог с тестами 
    - tests/test_create_ordeer.py  -  проверки на создания заказа
    - tests/test_create_user.py  -  проверки на создания пользователя
    - tests/test_get_order.py  -  проверки на получение заказа
    - tests/test_login_user.py  -  проверки на авторизацию пользователя
    - tests/test_update_user.py  -   проверки на изменения данных пользователя
    - tests/conftest.py  -  файл с фикстурами
    - data.py  -  файл с постоянными использукемыми в проверках
    - help.py  -  вспомогательные методы используемые в проверках


## Команды

Запустить тесты

    pytest tests --alluredir=allure_results

Посмотреть веб отчет

    allure serve allure_results

Посмотреть степень покрытия

    pytest --cov  