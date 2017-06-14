from aiohttp.web import Application


class Engine:
    app: Application

    def __init__(self):
        self.app = Application()
