import asyncio
from pathlib import Path
from aiohttp import web
import aiohttp_jinja2
import jinja2
import logging


routes = web.RouteTableDef()


@routes.get("/", name="root")
@aiohttp_jinja2.template('file.html')
async def get(request: web.Request):
    return {
        "processed_filename": request.query.get("processed_filename")
    }


@routes.post("/", name="root")
async def post(request: web.Request):
    data = await request.post()
    try:
        file: web.FileField = data['csv']
        with open('result.csv', "wb") as f:
            f.write(file.file.read())
        url = request.app.router['root'].url_for().with_query(
            {"processed_filename": file.filename}
        )
        raise web.HTTPFound(url)
    except KeyError:
        raise web.HTTPError


app = web.Application()
aiohttp_jinja2.setup(
    app=app,
    loader=jinja2.FileSystemLoader(Path(__file__).parent / "templates")
)
app.add_routes(routes)

logging.basicConfig(level=logging.DEBUG)
web.run_app(app, port=80)
