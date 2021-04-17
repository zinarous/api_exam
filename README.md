# A basic api using the CherryPy framework and Python 3.9.2.
# But before we start, it's better to taste delicious and tasty chicken!
![Kurochka KFC](https://github.com/zinarous/api_exam/blob/main/KFC.jpg)
# Build/Rebuild API Image
You may rebuild the server image:


```$ docker build -t api_final .```

```$ docker run -d -p 8080:8080 api_final```

# Build API tests Image

You may build and run tests (client part):


```$ docker build -t test_api .```

```$ docker run -d -p 8080:8080 test_api```

# Compose run
Run it as follows:

``` $ docker-compose up ```

Tests will start automatically

You can point your browser to http://localhost:8080/

There are database of users:

id
username
email
department
data_joined

Endpoints:
/api/users/
/api/department/
You can check all users by http://localhost:8080/api/users/ 
Also it has filters by 'username' and 'department'

For instance you can go to http://localhost:8080/api/users/alex and find user by this username or find username by the part of the name.
The same logic for department, by finding department find the usernames with this department.

You can check all departments by http://localhost:8080/api/department/ Also it has filter by 'department'

Finally you can stop the server as follows:

``` $ docker-compose down ```

# Show logs

To show logs open client CLI and use:

```$ cat tests.log```
