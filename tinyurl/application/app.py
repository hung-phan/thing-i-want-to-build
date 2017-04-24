import aiohttp_jinja2
import jinja2
import os
from aiohttp.web import run_app
from injector import inject

from application.controllers import ApplicationController
from application.engine import Engine
from application.middlewares import error_middleware


class App:
    engine: Engine
    application_controller: ApplicationController

    @inject
    def __init__(self,
                 engine: Engine,
                 application_controller: ApplicationController):
        self.engine = engine
        self.application_controller = application_controller

    def setup_templates(self):
        aiohttp_jinja2.setup(self.engine.app, loader=jinja2.PackageLoader("application", "templates"))

    def setup_routes(self):
        router = self.engine.app.router

        router.add_static("/static/", path=os.getcwd() + "/application/static", name="static")
        router.add_get("/", self.application_controller.index)
        router.add_post("/shorten_url", self.application_controller.create_shorten_url)

    def setup_middlewares(self):
        self.engine.app.middlewares.append(error_middleware)

    def setup_engine(self):
        run_app(self.engine.app, host="127.0.0.1", port=3000)

    def run(self):
        self.setup_templates()
        self.setup_routes()
        self.setup_middlewares()
        self.setup_engine()
