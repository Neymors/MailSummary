# MailSummary

Este proyecto toma noticias de un RSS, las resume utilizando Gemini, genera un PDF y lo envía por correo electrónico como una newsletter.

## Requisitos

- Python 3.x
- Librerías: gTTS, smtplib, reportlab, etc.

## Instalación

1. Clona este repositorio.
2. Instala las dependencias con `pip install -r requirements.txt`.
3. Configura las variables de entorno en el archivo `.env`.

## Uso

1. Modifica el archivo `main.py` para incluir las fuentes RSS que deseas procesar.
2. Ejecuta `main.py` para generar y enviar el boletín por correo electrónico.
