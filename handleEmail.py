import smtplib
from email.mime.text import MIMEText

#Config. server smtp
sender ="ferbeoulvedev@gmail.com"

recipients=[sender,"herrera.fernando1209@gmail.com"]
password="dhgj lxue zjfg tvjj"

def send_email(array):
     msg=MIMEText(body)
     msg['Subject']="Proceso Atrasado"
     msg['From']=sender
     msg['To']=', '.join(recipients)

     with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp_server:
          smtp_server.login(sender,password)
          
          for i in array:
               body="Auditoría/Proceso: "
               smtp_server.sendmail(sender, recipients,msg.as_string())
     print("Mensaje enviado con exito")
