from fastapi import FastAPI, Request 
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates

app = FastAPI() 
templates = Jinja2Templates(directory="templates")
name="Nicole"
skills=["AWS CLI","Git","Linux","Python","HTML"]

@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "name":name, "skills":skills})

