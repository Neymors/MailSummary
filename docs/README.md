# 🛰️  MailSummary

**MailSummary** es una aplicación automatizada que:

1. 📡 Recolecta noticias desde múltiples fuentes RSS.
2. 🧠 Resume los contenidos utilizando modelos de lenguaje como Gemini.
3. 🧾 Genera un documento PDF con los resúmenes.
4. 📬 Envía el reporte por email como una newsletter.

---

## 🚀 Tecnologías usadas

- Python 3.10
- `gTTS`, `smtplib`, `email`, `fpdf`
- Modelos LLM (Gemini API)
- `.env` para variables de entorno

---

## 📂 Estructura del proyecto
MailSummary/ │ 
├── core/ │ 
├── app.py # Lógica principal │ 
├── cliente.py # Consulta a fuentes RSS │ 
├── resumen.py # Resumen con Gemini │ 
├── pdf_generator.py # Generación de PDF │ 
├── mail_sender.py # Envío por email │ 
├── mail.env # Credenciales de mail │ 
└── Resumenes/ # PDFs generados │ 
├── .gitignore 
├── README.md 
└── main.py

---

## 🛠️ Cómo correrlo

1. Cloná el repo  
   ```bash
https://github.com/Neymors/MailSummary   
cd MailSummary
python core/main.py
