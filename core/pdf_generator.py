from fpdf import FPDF
import unicodedata

def limpiar_texto(texto):
    # Elimina caracteres especiales y convierte a ASCII plano
    texto_normalizado = unicodedata.normalize('NFKD', texto)
    return texto_normalizado.encode('ascii', 'ignore').decode('ascii')

def generar_pdf(texto, nombre_archivo="resumen.pdf"):
    if not texto or not isinstance(texto, str):
        raise ValueError("El texto proporcionado para el PDF está vacío o no es válido.")

    try:
        texto_limpio = limpiar_texto(texto)  # <- Limpiamos los caracteres problemáticos

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for linea in texto_limpio.split('\n'):
            pdf.multi_cell(0, 10, linea)

        pdf.output(nombre_archivo)
        print(f"PDF generado correctamente: {nombre_archivo}")
        return nombre_archivo

    except Exception as e:
        raise RuntimeError(f"Error al generar el PDF: {e}")
