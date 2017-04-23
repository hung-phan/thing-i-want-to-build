from injector import inject
from aiohttp.web import Application, run_app


class Engine:
    _app: Application

    def __init__(self):
        self._app = Application()

    @property
    def app(self):
        return self._app


class MainApp:
    _engine: Engine

    @inject
    def __init__(self, engine: Engine):
        self._engine = engine

    def setup_routes(self):
        router = self._engine.app.router

    def run(self):
        self.setup_routes()

        run_app(self._engine.app, host="127.0.0.1", port=3000)
