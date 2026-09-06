import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_ADDRESS = os.environ["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
RECIPIENT_EMAIL = os.environ.get("RECIPIENT_EMAIL", GMAIL_ADDRESS)


def build_body(paper: dict) -> str:
    meta_line = f"Categoría: {paper.get('category', 'sin categoría')}"
    if paper.get("journal"):
        meta_line += f" | Revista: {paper['journal']}"
    if paper.get("year"):
        meta_line += f" | Año: {paper['year']}"

    header = (
        f"📄 {paper['title']}\n"
        + (f"Autores: {paper['authors']}\n" if paper.get("authors") else "")
        + meta_line + "\n"
        + (f"Enlace: {paper['url']}\n" if paper.get("url") else "")
        + (f"Nota tuya: {paper['notes']}\n" if paper.get("notes") else "")
        + ("\n" + "-" * 50 + "\n\n")
    )

    sections = (
        f"**Resumen**\n{paper.get('resumen', '')}\n\n"
        f"**Implicaciones**\n{paper.get('implicaciones', '')}\n\n"
        f"**Preguntas abiertas para reflexionar**\n{paper.get('preguntas_abiertas', '')}\n\n"
        f"**Campo de estudio**\n{paper.get('campo_estudio', '')}\n"
    )

    return header + sections


def send_daily_paper(paper: dict):
    body = build_body(paper)
    msg = MIMEMultipart()
    msg["From"] = GMAIL_ADDRESS
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = f"📚 Paper del día: {paper['title'][:80]}"
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(msg)
