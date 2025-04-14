from fpdf import FPDF
import unicodedata
from datetime import datetime

def limpiar_texto(texto):
    """
    Elimina caracteres especiales y convierte a ASCII plano.
    """
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    return texto_normalizado.encode('ascii', 'ignore').decode('ascii')

class PDFResumen(FPDF):
    def header(self):
        # Encabezado: Título y fecha centrada.
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(33, 37, 41)  # Gris oscuro
        self.cell(0, 10, "Resumen de Noticias", ln=True, align="C")
        self.set_font("Helvetica", "", 12)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, datetime.now().strftime("%d/%m/%Y"), ln=True, align="C")
        self.ln(5)
        # Línea divisoria
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def footer(self):
        # Pie de página: Texto centrado.
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, "MailSummary · Automatizado con ", 0, 0, "C")

def generar_pdf(texto, nombre_archivo="resumen.pdf"):
    """
    Genera un PDF a partir de un texto dado.
    - Limpia el texto (eliminando caracteres especiales).
    - Añade un header con título y fecha.
    - Añade un footer con información de MailSummary.
    - Escribe el texto en el cuerpo del PDF.
    
    Parámetros:
      texto: str, el contenido a incluir en el PDF.
      nombre_archivo: str, nombre del archivo PDF a generar.
    
    Retorna:
      El nombre del archivo PDF generado.
    """
    if not texto or not isinstance(texto, str):
        raise ValueError("El texto proporcionado para el PDF está vacío o no es válido.")

    try:
        texto_limpio = limpiar_texto(texto)

        pdf = PDFResumen()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)
        pdf.set_text_color(60, 60, 60)

        # Escribir línea por línea el texto limpio
        for linea in texto_limpio.split('\n'):
            pdf.multi_cell(0, 10, linea)

        pdf.output(nombre_archivo)
        print(f"PDF generado correctamente: {nombre_archivo}")
        return nombre_archivo

    except Exception as e:
        raise RuntimeError(f"Error al generar el PDF: {e}")

# Ejemplo de uso:
if __name__ == "__main__":
    texto_ejemplo = """Noticia 1: Esto es un ejemplo de una noticia.
Segunda línea de la noticia.
    
Noticia 2: Otra noticia interesante que se resume en estas líneas."""
    generar_pdf(texto_ejemplo, "resumen.pdf")
