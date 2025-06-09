import data_generation

class Urls:
    # страница сервиса
    URL = 'https://qa-scooter.praktikum-services.ru'

class Api:
    # API курьера
    LOGIN_COURIER_API = '/api/v1/courier/login' #POST
    CREATE_COURIER_API = '/api/v1/courier' #POST
    DELETE_COURIER_API = '/api/v1/courier/' #DELETE
    # API заказа
    CREATE_ORDER_API = '/api/v1/orders'  #POST
    CANCEL_ORDER_API = '/api/v1/orders/cancel' #PUT
    GET_ORDERS_LIST_API = '/api/v1/orders' #GET

class OrderData:
    order_body = {
        'firstName': 'Naruto',
        'lastName': 'Uchiha',
        'address': 'Konoha, 142 apt.',
        'metroStation': 4,
        'phone': '+7 800 355 35 35',
        'rentTime': 5,
        'deliveryDate': '2025-06-06',
        'comment': 'Saske, come back to Konoha',
        'color': []
    }
    color = [[''], ['BLACK'], ['GREY'], (['BLACK'], ['GREY'])]
    success_create_order = 'track'
    success_response_order = 'orders'

class Response:
    SUCCESS_CREATE_COURIER = {'ok': True}
    CONFLICT_CREATE_COURIER = {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
    BED_REQ_CREATE_COURIER = {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}
    NOT_FOUND_COURIER = {'code': 404, 'message': 'Учетная запись не найдена'}
    BED_REQ_LOGIN_COURIER = {'code': 400, 'message': 'Недостаточно данных для входа'}

class Courier:
    reg_data = [{'login': data_generation.courier_registration_data()['login'], 'firstName': data_generation.courier_registration_data()['firstName']},
                {'password': data_generation.courier_registration_data()['password'], 'firstName': data_generation.courier_registration_data()['firstName']},
                {'login': data_generation.courier_registration_data()['login'], 'password': data_generation.courier_registration_data()['password']}]
