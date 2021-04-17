import pytest
import requests

passed='Passed'
failed='Failed'

def logs(func_name, status, error='No errors'):
    with open('tests.log', 'a+', encoding='utf-8') as f1:
        line=f'{func_name}, {status}, {error}\n'
        f1.writelines(line)


def test_users():
    func_name = test_users.__name__
    r = requests.get('http://127.0.0.1:8080/api/users')
    if r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, \
        {'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, \
        {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, \
        {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}, \
        {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]":
        logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_users_zero():
    func_name = test_users_zero.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/0')
    if r.text == "data: []":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: []"

def test_username_v():
    func_name = test_username_v.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/v')
    if r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}]"

def test_username_x():
    func_name = test_username_x.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/x')
    if r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_username_alex():
    func_name = test_username_alex.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/alex')
    if r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}]"

def test_department_DTS():
    func_name = test_department_DTS.__name__
    r = requests.get('http://127.0.0.1:8080/api/users?department=DTS')
    if r.text == "data: [{'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}]"

def test_department_ART():
    func_name = test_department_ART.__name__
    r = requests.get('http://127.0.0.1:8080/api/users?department=ART')
    if r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_department_user():
    func_name = test_department_user.__name__
    r = requests.get('http://127.0.0.1:8080/api/users?department=A&username=m')
    if r.text == "data: [{'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_department_F():
    func_name = test_department_F.__name__
    r = requests.get('http://127.0.0.1:8080/api/users?department=F')
    if r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}]"

def test_department_u():
    func_name = test_department_u.__name__
    r = requests.get('http://127.0.0.1:8080/api/users/max/D')
    if r.text == "data: [{'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}]"

def test_departments():
    func_name = test_departments.__name__
    r = requests.get('http://127.0.0.1:8080/api/department')
    if r.text == "Here all departments: ['ART', 'DTS', 'FRS', 'LevelART']":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "Here all departments: ['ART', 'DTS', 'FRS', 'LevelART']"

def test_departments_L():
    func_name = test_departments_L.__name__
    r = requests.get('http://127.0.0.1:8080/api/department/L')
    if r.text == "data: [{'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]"

def test_departments_FRS():
    func_name = test_departments_FRS.__name__
    r = requests.get('http://127.0.0.1:8080/api/department/FRS')
    if r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}]":
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Text request doesn't match the text in DB") 
    assert r.text == "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}]"

def test_ok_users():
    func_name = test_ok_users.__name__
    if "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]" == requests.get('http://127.0.0.1:8080/api/users'):
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Response == 200") 
    assert "data: [{'username': 'van', 'email': 'vano@yandex.ru', 'department': 'FRS', 'date_joined': '2021-01-20'}, {'username': 'alex', 'email': 'zinar@mail.ru', 'department': 'ART', 'date_joined': '2021-01-26'}, {'username': 'max', 'email': 'mman@gmail.com', 'department': 'DTS', 'date_joined': '2021-05-20'}, {'username': 'san', 'email': 'mman@gmail.com', 'department': 'FRS', 'date_joined': '2020-08-25'}, {'username': 'max', 'email': 'mmansss@gmail.com', 'department': 'LevelART', 'date_joined': '2020-05-20'}]" == requests.get('http://127.0.0.1:8080/api/users')

def test_ok_departament():
    func_name = test_ok_departament.__name__
    if "Here all departments: ['ART', 'DTS', 'FRS', 'LevelART']" == requests.get('http://127.0.0.1:8080/api/department'):
            logs(func_name, passed)
    else:
        logs(func_name, failed, "Response == 200") 
    assert "Here all departments: ['ART', 'DTS', 'FRS', 'LevelART']" == requests.get('http://127.0.0.1:8080/api/department')

