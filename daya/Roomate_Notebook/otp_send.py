import smtplib

class mail_send:
    def __init__(self,username,password):
        self.username = username
        self.pw = password
        self.mail_obj = smtplib.SMTP('smtp.gmail.com',587)

    def login_mail(self):
        try:

            self.mail_obj.starttls()
            self.mail_obj.login(self.username,self.pw)

            return True
        except Exception as E:

            return False
    def send_mail(self,to,otp):
        try:
            if self.login_mail():
                self.to = to
                self.msg = f'Forget password OTP:{otp}'
                self.mail_obj.sendmail(self.username,self.to,self.msg)

                self.mail_obj.quit()
        except Exception as E:

            return False