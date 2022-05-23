import email
import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from']='wxy name' ##sender
email['to']='wxy id'   ##reciever
email['subject']='wxy subject'
email.set_content("wxy content of email")
with smtplib.SMTP(host='smtp.gmail.com',port=587)as smtp: 
  smtp.ehlo()  
  smtp.starttls()   
  smtp.send_message(email)
  print("email send") 
