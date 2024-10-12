from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil  # Para guardar archivos cargados temporalmente

app = FastAPI()

# Montar archivos estáticos (CSS, imágenes, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Plantillas Jinja2
templates = Jinja2Templates(directory="templates")

# Endpoint para la página principal
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint para procesar la imagen subida
@app.post("/procesar-imagen/")
async def procesar_imagen(file: UploadFile = File(...)):
    # Guardar el archivo temporalmente
    file_location = f"temp/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)



    return {"info": f"Archivo '{file.filename}' subido con éxito."}
