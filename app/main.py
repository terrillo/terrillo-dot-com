from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="/static"), name="static")

templates = Jinja2Templates(directory="/code/app/templates")


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("home.jinja", {"request": request})


@app.exception_handler(404)
async def custom_404_handler(_, __):
    return RedirectResponse("/")
