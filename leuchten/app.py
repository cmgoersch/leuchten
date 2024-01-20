from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from leuchten.logging import logger

app = FastAPI(title='leuchten', version='0.1.0')

app.mount('/static', StaticFiles(directory='static'), name='static')

templates = Jinja2Templates(directory='templates')


@app.get('/', response_class=HTMLResponse)
async def leuchten_status(request: Request):
    logger.info('new request')
    return templates.TemplateResponse(
        request=request,
        name='index.html.j2',
        context={'status': 'open', 'hours': 1, 'minutes': 13, 'seconds': 50},
    )
