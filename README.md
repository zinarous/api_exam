# A basic api using the CherryPy framework and Python 3.9.2.
# Run
Run it as follows:

``` $ docker-compose up ```

Tests will start automatically

You can point your browser to http://locahost:8080/

There are database of users:

id
username
email
department
data_joined
Endpoints:

/users/
/department/
You can check all users by http://locahost:8080/users/ Also it has filters by 'username' and 'department'

You can check all departments by http://locahost:8080/department/ Also it has filter by 'department'

Finally you can stop the server as follows:

``` $ docker-compose down ```

# Build/Rebuild
You may rebuild the server image:


```$ docker build -t api-start .```

```$ docker run -d -p 8080:8080 api-start```

# Run tests

You may build and run tests (client part):


```$ docker build -t api-tests .```

```$ docker run -d -p 8080:8080 api-tests```

# Show logs

To show logs open client CLI and use:

```$ cat tests.log```
