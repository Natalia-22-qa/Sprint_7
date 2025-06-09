import random
import string

# метод регистрации нового курьера возвращает словарь из логина, пароля и имени
def courier_registration_data():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    # собираем тело запроса
    login_pass = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    # возвращаем словарь
    return login_pass
