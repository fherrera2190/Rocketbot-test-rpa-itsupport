import smtplib
from email.mime.text import MIMEText
from smtplib import SMTPRecipientsRefused
#Config. server smtp
sender ="ferbeoulvedev@gmail.com"
password="dhgj lxue zjfg tvjj"
coding="utf-8"
def send_email(array):
     smtp_server= smtplib.SMTP_SSL('smtp.gmail.com',465)
     try:
          smtp_server.login(sender,password)
          for i in array:
               body="Auditoría/Proceso: "+i[0]+"\nEstado: "+i[9]+"\nObervación: "+i[1]+"\nFecha de compromiso: "+i[5].strftime("%Y-%m-%d %H:%M:%S")
               msg=MIMEText(body,'plain', _charset=coding)
               msg['Subject']="Proceso Atrasado"
               msg['From']=sender
               msg['To']=i[8].replace(" ", "")
               print("Enviando a ",msg['To'])
               smtp_server.sendmail(sender,msg['To'],msg.as_string())
               print("Mensaje enviado con exito")
     except  SMTPRecipientsRefused as e:
        print("Error al Mandar msj")
       # print("Error al enviar correo electrónico a", recipient)
        print("Detalles del error:", e)
     finally:
          smtp_server.quit()
          
     
    
