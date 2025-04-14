import smtplib
from email.message import EmailMessage
import os

def enviar_email(destinatario, archivo_adjunto):
    remitente = os.environ.get("EMAIL_REMITENTE")
    password = os.environ.get("EMAIL_PASSWORD")

    if not remitente or not password:
        raise ValueError("No se encontraron las variables de entorno EMAIL_REMITENTE o EMAIL_PASSWORD")

    mensaje = EmailMessage()
    mensaje["Subject"] = "Resumen de Noticias"
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje.set_content("Adjunto el resumen de noticias en formato PDF.")

    # Adjuntar archivo PDF
    with open(archivo_adjunto, "rb") as f:
        pdf_data = f.read()
        mensaje.add_attachment(pdf_data, maintype="application", subtype="pdf", filename=archivo_adjunto)

    # Enviar el correo
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(remitente, password)
        smtp.send_message(mensaje)
