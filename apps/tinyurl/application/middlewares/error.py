import aiohttp_jinja2
from aiohttp.web import HTTPException
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from typing import Dict, Callable


async def handle_404(request: Request, response: Response):
    return aiohttp_jinja2.render_template('404.html', request, {})


async def handle_422(request: Request, response: Response):
    return aiohttp_jinja2.render_template('422.html', request, {})


async def handle_500(request: Request, response: Response):
    return aiohttp_jinja2.render_template('500.html', request, {})


def error_pages(overrides: Dict[int, Callable]):
    async def middleware(_, handler):
        async def middleware_handler(request: Request):
            try:
                response = await handler(request)
                override = overrides.get(response.status)
                if override is None:
                    return response
                else:
                    return await override(request, response)
            except HTTPException as ex:
                override = overrides.get(ex.status)
                if override is None:
                    raise
                else:
                    return await override(request, ex)

        return middleware_handler

    return middleware


error_middleware = error_pages({404: handle_404, 422: handle_422, 500: handle_500})
