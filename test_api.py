import pytest
import api_final
import requests


@pytest.fixture
def server():
    serv = api_final.serv_start()
    serv.engine.start()
    serv.engine.wait(serv.engine.states.STARTED)

    yield
    
    serv.engine.exit()
    serv.engine.block()

def test_users(server):
    r = requests.get('http://127.0.0.1:8080/api/users')
    assert r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_users_zero(server):
    r = requests.get('http://127.0.0.1:8080/api/users/0')
    assert r.text == "data: []"


def test_username_v(server):
    r = requests.get('http://127.0.0.1:8080/api/users/v')
    assert r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}]"

def test_username_x(server):
    r = requests.get('http://127.0.0.1:8080/api/users/x')
    assert r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_username_alex(server):
    r = requests.get('http://127.0.0.1:8080/api/users/alex')
    assert r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}]"

def test_department_DTS(server):
    r = requests.get('http://127.0.0.1:8080/api/users?department=DTS')
    assert r.text == "data: [{'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}]"

def test_department_ART(server):
    r = requests.get('http://127.0.0.1:8080/api/users?department=ART')
    assert r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_department_user(server):
    r = requests.get('http://127.0.0.1:8080/api/users?department=A&username=m')
    assert r.text == "data: [{'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_department_F(server):
    r = requests.get('http://127.0.0.1:8080/api/users?department=F')
    assert r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}]"

def test_department_u(server):
    r = requests.get('http://127.0.0.1:8080/api/users/max/D')
    assert r.text == "data: [{'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}]"

def test_departments(server):
    r = requests.get('http://127.0.0.1:8080/api/department')
    assert r.text == "Here all departments: ['ART', 'DTS', 'FRS', 'LevelART']"

def test_departments_L(server):
    r = requests.get('http://127.0.0.1:8080/api/department/L')
    assert r.text == "data: [{'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_departments_FRS(server):
    r = requests.get('http://127.0.0.1:8080/api/department/FRS')
    assert r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}]"

def test_ok_users(server):
    assert "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]" == requests.get('http://127.0.0.1:8080/api/users')

def test_ok_departament(server):
    assert "Here all departments: ['ART', 'DTS', 'FRS', 'LevelART']" == requests.get('http://127.0.0.1:8080/api/department')

