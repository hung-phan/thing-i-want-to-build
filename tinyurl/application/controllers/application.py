import aiohttp_jinja2 as aiohttp_jinja2
from aiohttp.web_request import Request
from aiohttp.web_response import Response, json_response
from injector import inject

from domain.models import URL
from domain.repositories import URLRepository


class ApplicationController:
    url_repository: URLRepository

    @inject
    def __init__(self, url_repository: URLRepository):
        self.url_repository = url_repository

    @aiohttp_jinja2.template("index.html")
    async def index(self, _):
        return {}

    async def create_shorten_url(self, request: Request):
        params = await request.post()
        url = await self.url_repository.find_by("original_url", params["original_url"])

        if not url:
            url = await self.url_repository.create(
                URL(original_url=params["original_url"])
            )

        return json_response({
            "id": url.id,
            "original_url": url.original_url,
            "expire_time": str(url.expire_time)
        })

    async def redirect(self, request: Request):
        params = request.match_info
        url = await self.url_repository.find_by("id", params["shorten_url"])

        if url:
            return Response(
                status=302,
                headers={
                    "location": url.original_url
                }
            )
        else:
            return Response(status=404)
