from email.mime.text import MIMEText

import smtplib

def send_email(email,height,average_height,count):
        from_email="tuannguyenanh_lido1995@yahoo.com.vn"
        from_password="12345678@T"
        to_email="nguyenanhtuan92my@gmail.com"
        debuglevel = True
        subject="Height data"
        message= " Hey there, your height is <strong>%s</strong>. <br> Average height of all is <strong>%s</strong> and that is calculated out of <strong>%s</strong> people. <br> Thanks! " %(height,average_height,count)

        msg = MIMEText(message,'html')
        msg['Subject'] = subject
        msg['To'] = to_email
        msg['From'] = from_email

        try:
            yhmail = smtplib.SMTP('smtp.mail.yahoo.com',587)
            yhmail.ehlo()
            yhmail.set_debuglevel(debuglevel)
            yhmail.starttls()
            yhmail.login(from_email,from_password)
            #yhmail.send_message(msg)
            yhmail.sendmail(from_email,to_email, msg.as_string())
            print("ok the email has sent")
        except :
            print('can\'t send the Email')
