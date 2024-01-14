import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'your_smtp_server'  # 例如 'smtp.gmail.com'
SMTP_PORT = 587  # 通常的SMTP端口
SMTP_USERNAME = 'your_email@example.com'  # 你的邮箱地址
SMTP_PASSWORD = 'your_email_password'  # 你的邮箱密码

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email sending failed: {e}")
        return False
