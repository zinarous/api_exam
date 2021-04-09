import cherrypy

users = {
    '1': {
        'username': 'van',
        'email': 'vano@yandex.ru',
        'department': 'FRS',
        'date_joined': '2021-01-20'
    },
    '2': {
        'username': 'alex',
        'email': 'zinar@mail.ru',
        'department': 'ART',
        'date_joined': '2021-01-26'
    },
    '3': {
        'username': 'max',
        'email': 'mman@gmail.com',
        'department': 'DTS',
        'date_joined': '2021-05-20'
    },
    '4': {
        'username': 'san',
        'email': 'mman@gmail.com',
        'department': 'FRS',
        'date_joined': '2020-08-25'
    },
    '5': {
        'username': 'max',
        'email': 'mmansss@gmail.com',
        'department': 'LevelART',
        'date_joined': '2020-05-20'
    },
}

class Users:
    def GET(self, username=None, department=None):
        data1 = []
        data2 = []
        if username == None:
            for user in users:
                data1.append(users[user])
        else:
            for user in users:
                if username in users[user]['username']:
                    data1.append(users[user])

        if department == None:
            for deps in users:
                data2.append(users[deps])
        else:
            for deps in users:
                if department in users[deps]['department']:
                    data2.append(users[deps])

        data3 = []
        for item in data1:
            if item in data2:
                data3.append(item)
        return ('data: %s' % data3)

    exposed = True

class Deps:
    def GET(self, department=None):
        data1 = []
        
        if department == None:
            for deps in users:
                data1.append(users[deps]["department"])
            return ('Here all departments: %s' % list(set(data1)))
        else:
            for deps in users:
                if department in users[deps]['department']:
                    data1.append(users[deps])

        return ('data: %s' % data1)
    exposed = True

if __name__ == '__main__':

    cherrypy.tree.mount(
        Users(), '/api/users',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.tree.mount(
        Deps(), '/api/department',
        {'/':
            {'request.dispatch': cherrypy.dispatch.MethodDispatcher()}
        }
    )

    cherrypy.engine.start()
    cherrypy.engine.block()
