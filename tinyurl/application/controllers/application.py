import aiohttp_jinja2 as aiohttp_jinja2
from aiohttp.web_request import Request
from injector import inject

from domain.repositories import URLRepository


class ApplicationController:
    url_repository: URLRepository

    @inject
    def __init__(self, url_repository: URLRepository):
        self.url_repository = url_repository

    @aiohttp_jinja2.template("index.html")
    async def index(self, request: Request):
        return {}

    async def create(self, request: Request):
        print(request)
