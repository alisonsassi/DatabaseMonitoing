import smtplib
import email.message
import logging

def send_email(subject,body):  
    corpo_email = "<p>" + body + "</p>"
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = 'sendere23@gmail.com'
    msg['To'] = 'alison.sassi@philips.com'
    password =  'zhvjsbdgulzbuzmb' # Login: sendere23@gmail.com Password: 23Philips@ 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))

    logging.info("Enviado o e-mail" + str(msg))