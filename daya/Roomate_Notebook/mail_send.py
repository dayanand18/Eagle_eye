
import smtplib
class send_msg:

    def __init__(self,user,passwo):
        self.user = user
        self.pw = passwo


    def email_login(self):
        try:
            self.em = smtplib.SMTP("smtp.gmail.com",587)
            self.em.starttls()
            self.em.login(self.user,self.pw)
            print("login")
            return True
        except Exception as E:
            print(E)
            return False
    def send_mail(self,to,msg):
        try:
            if self.email_login():
                self.em.sendmail(self.user,to,msg)
                print("send success")
                return True
            return False
        except:
            return False
# obj = send_msg("daya.ba007@gmail.com","actionkingshashi")
# # obj.send_mail('sweetshashipatil',"aram Dosta...!")
# obj.email_login()


