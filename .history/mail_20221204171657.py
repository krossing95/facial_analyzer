import smtplib
from templates import acc_verification, plTemplate
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import smtplib
import ssl

SERVER = "smtp.office365.com"
FROM = "explicitserver95@hotmail.com"
PASSWORD = "Krossing@1995"
PORT = 587
msg = MIMEMultipart()


def transitAccVerification(receiver, subject, link, name):
    template = acc_verification(link=link, name=name)
    msg['From'] = formataddr(('Smart Attendance System Team', FROM))
    msg['To'] = formataddr((name, receiver))
    msg['Subject'] = subject
    msg.attach(MIMEText(template, "html"))
    messageBody = msg.as_string()
    SSLcontext = ssl.create_default_context()
    with smtplib.SMTP(SERVER, PORT) as server:
        server.starttls(context=SSLcontext)
        server.login(user=FROM, password=PASSWORD)
        try:
            sent = server.sendmail(FROM, receiver, messageBody)
            server.quit()
            return sent
        except:
            return False
# def mailPl(receiver, subject, link, name):
# 	template = plTemplate(link=link)
# 	msg['From'] = formataddr(('Smart Attendance System Team', FROM))
# 	msg['To']= formataddr((name, receiver))
# 	msg['Subject']= subject
# 	msg.attach(MIMEText(template, "html"))
# 	messageBody = msg.as_string()
# 	SSLcontext = ssl.create_default_context()
# 	with smtplib.SMTP(SERVER, PORT) as server:
# 		server.starttls(context=SSLcontext)
# 		server.login(user = FROM, password = PASSWORD)
# 		try:
# 			return server.sendmail(FROM, receiver, messageBody)
# 		except:
# 			return False
