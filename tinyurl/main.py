from injector import Injector

from application.app import App

injector = Injector()

if __name__ == '__main__':
    injector.get(App).run()
