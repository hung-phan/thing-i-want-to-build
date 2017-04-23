from application.web import MainApp
from injector import Injector

injector = Injector()

if __name__ == '__main__':
    injector.get(MainApp).run()
