
from fastapi import FastAPI, File, UploadFile  #gestionar los archivos subidos por el usuario.
from fastapi.responses import HTMLResponse
from PIL import Image   #  PIL (a través de Pillow) para cargar y manipular imágenes.
import pytesseract #biblioteca de Python que usa Tesseract OCR para extraer texto de las imágenes.
import cv2  #para procesar las imágenes antes de pasarlas a Tesseract (convertir a escala de grises, binarización, 
import numpy as np # NumPy para convertir las imágenes a matrices que OpenCV puede procesar.
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

@app.get("/")
def read_route():
    return {"Mensaje": "Prueba Ok"}


app.mount("/static", StaticFiles(directory="app/static"), name="static")
