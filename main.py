import logging
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from core import BASE_DIR, templates
from routes import home, jewelry, party

log = logging.getLogger("pocketsmart")
app = FastAPI(title="PocketSmart AI")
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
app.include_router(home.router)
app.include_router(party.router)
app.include_router(jewelry.router)


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "index.html", {})


@app.exception_handler(StarletteHTTPException)
async def http_error(request: Request, exc: StarletteHTTPException):
    msg = "Page not found." if exc.status_code == 404 else "Something went wrong."
    return templates.TemplateResponse(request, "error.html", {"message": msg, "code": exc.status_code}, status_code=exc.status_code)


@app.exception_handler(Exception)
async def server_error(request: Request, exc: Exception):
    log.exception("Unhandled error")  # traceback goes to terminal only
    return templates.TemplateResponse(request, "error.html", {"message": "Something went wrong. Please try again.", "code": 500}, status_code=500)
