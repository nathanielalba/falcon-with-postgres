import falcon

from database.main import DatabaseManager

class App(falcon.API):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__(*args, **kwargs)

        print('Application is now starting..')


manager = DatabaseManager()
db = manager.initDB()
application = App()

if __name__ == "__main__":
    from wsgiref import simple_server
    server = simple_server.make_server('127.0.0.1', 4000, application)
    print('Application is now running on port :4000')
    server.serve_forever()
