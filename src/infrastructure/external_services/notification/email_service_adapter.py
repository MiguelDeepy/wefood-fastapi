from typing import Dict
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from app.domain.ports.notification_service import NotificationService


class EmailServiceAdapter(NotificationService):
    def __init__(self, smtp_config: Dict):
        self.smtp_config = smtp_config

    async def enviar_notificacao(self, destinatario: str, assunto: str, mensagem: str):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.smtp_config['from']
            msg['To'] = destinatario
            msg['Subject'] = assunto

            msg.attach(MIMEText(mensagem, 'plain'))

            server = smtplib.SMTP(self.smtp_config['host'], self.smtp_config['port'])
            server.starttls()
            server.login(self.smtp_config['user'], self.smtp_config['password'])
            server.send_message(msg)
            server.quit()
        except Exception as e:
            raise Exception(f"Erro ao enviar email: {str(e)}")
