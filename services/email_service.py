import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config.settings import EMAIL_CONFIG

class EmailService:
    def __init__(self):
        self.smtp_server = EMAIL_CONFIG['SMTP_SERVER']
        self.smtp_port = EMAIL_CONFIG['SMTP_PORT']
        self.sender_email = EMAIL_CONFIG['SENDER_EMAIL']
        self.sender_password = EMAIL_CONFIG['SENDER_PASSWORD']

    def send_email(self, recipient_email, subject, body):
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password)
            server.sendmail(self.sender_email, recipient_email, message.as_string())
