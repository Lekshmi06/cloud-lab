from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

app = FastAPI()

# Mount static files (CSS, images, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load HTML templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

# Run with: uvicorn main:app --reload

# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# # Mount the static folder for CSS/JS files
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Set up Jinja2 templates
# templates = Jinja2Templates(directory="templates")



# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

# app = FastAPI()

# # Setup static files for CSS
# app.mount("/static", StaticFiles(directory="static"), name="static")

# # Setup Jinja2 templates
# templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def home(request: Request):
#     return templates.TemplateResponse("home.html", {"request": request})

# @app.get("/about")
# async def about(request: Request):
#     return templates.TemplateResponse("about.html", {"request": request})

# @app.get("/contact")
# async def contact(request: Request):
#     return templates.TemplateResponse("contact.html", {"request": request})

# @app.get("/dashboard")
# async def dashboard(request: Request):
#     return templates.TemplateResponse("dashboard.html", {"request": request})