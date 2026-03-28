from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import qr, ui

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")


# Routers Registers (Apps if in Django)
#app.include_router(home.router)
#app.include_router(items.router)
app.include_router(qr.router)
app.include_router(ui.router)