
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from languages import langs

app = FastAPI()

app.mount('/static', StaticFiles(directory= 'static'), name = 'static')

templates = Jinja2Templates(directory='templates')

@app.get('/signup', response_class=HTMLResponse)
def signUp(request : Request):
    return templates.TemplateResponse(
        'signup.html',
        {'request': request, 
         'lang_data': langs.load_lang_data(page_name='signup_page', lang='fr')
        }
    )