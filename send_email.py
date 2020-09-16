import smtplib

import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, message)
        server.quit()
        print("Sucess: Email sent!")
    except:
        print("Email failed to send.")
        
subject = "Test subject"
msg = "message of the Email"

send_email(subject, msg)
