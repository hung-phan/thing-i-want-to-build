from aiohttp.web import Application


class Engine:
    _app: Application

    def __init__(self):
        self._app = Application()

    @property
    def app(self):
        return self._app
