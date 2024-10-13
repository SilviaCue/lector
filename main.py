from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil  # Para guardar archivos cargados temporalmente
import numpy as np
import cv2
from PIL import Image
import pytesseract

app = FastAPI()

# Montar archivos estáticos (CSS, imágenes, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Plantillas Jinja2
templates = Jinja2Templates(directory="templates")

# Endpoint para la página principal
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# Endpoint para procesar imágenes
@app.post("/procesar-imagen/")
async def procesar_imagen(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Preprocesar la imagen
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img_proc = cv2.threshold(gris, 150, 255, cv2.THRESH_BINARY)

        # Realizar OCR
        preprocessed_img = Image.fromarray(img_proc)
        texto = pytesseract.image_to_string(preprocessed_img, lang='spa')

        return {"texto_extraido": texto}

    except Exception as e:
        return {"error": str(e)}