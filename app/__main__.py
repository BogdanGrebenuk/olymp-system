from aiohttp import web

from app.main import create_app
from app.settings import config


app = create_app()
host = config['app']['host']
port = config['app']['port']
web.run_app(app, host=host, port=port)
