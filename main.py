from typing import Annotated
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfWriter, PdfReader
import io
from starlette.responses import StreamingResponse
from datetime import datetime

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
pdfmetrics.registerFont(TTFont('Montserrat', 'style/fonts/Montserrat-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Montserrat-Italic', 'style/fonts/Montserrat-Italic.ttf'))
months = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

def write_name(name: str, name_buffer: io.BytesIO, date: str | None = None):
    c = canvas.Canvas(name_buffer)

    c.setFont("Montserrat", 26)
    c.setFillColorRGB(1, 1, 1)
    c.drawCentredString(421, 335, name)

    if date is not None:
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        day = parsed_date.day
        month = parsed_date.month
        year = parsed_date.year

        if 1 <= month <= 12:
            c.setFont("Montserrat-Italic", 12)
            c.setFillColorRGB(0, 0, 0)
            c.drawCentredString(421, 196.5, f"Entregue em {day} de {months[month - 1]} de {year}.")

    c.save()
    name_buffer.seek(0)

def merge_pdfs(name_buffer: io.BytesIO, output_buffer: io.BytesIO):
    cert_pdf = PdfReader("templates/certificate_template.pdf")
    cert_page = cert_pdf.pages[0]

    name_pdf = PdfReader(name_buffer)
    name_page = name_pdf.pages[0]

    writer = PdfWriter()
    page = writer.add_page(cert_page)
    page.merge_page(name_page)
    writer.add_page(cert_pdf.pages[1])
    writer.write(output_buffer)
    output_buffer.seek(0)

@app.post("/certificate/")
async def generate_certificate(name: Annotated[str, Form()], date: Annotated[str | None, Form()] = None):
    output_buffer = io.BytesIO()
    name_buffer = io.BytesIO()

    write_name(name, name_buffer, date)
    merge_pdfs(name_buffer, output_buffer)
    return StreamingResponse(output_buffer, media_type="application/pdf")

@app.get("/")
def index():
     return FileResponse("static/index.html")



