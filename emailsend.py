from email.message import EmailMessage
from validate_email_address import validate_email
import ssl
import smtplib
email_sender='shrutikdawane@gmail.com'
email_password='fodfvstkmcdhtbqh'

email_receiver=input("enter the email you want to send email too")
if validate_email(email_receiver)==True:
    print("email vaild")
else:
    print("enter the vaild email")
    exit()

subj=input("enter the subject:")
body=input("enter the message you want to send: ")
em=EmailMessage()
em['From']=email_sender
em['To']=email_receiver
em['subject']=subj
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL( 'smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())