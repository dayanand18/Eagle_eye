
from email.encoders import encode_base64
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP


def send_mail(To,mnth,report,name,username='dayaayb@gmail.com',password='daya7090'):
    try:
        message = MIMEMultipart()
        message['Subject'] = "Room Rent Receipt-"+str(mnth)
        message['From'] = f'{username}'
        message['Reply-to'] = 'get'
        message['To'] = f'{To}'

        Msg = MIMEText(f"Dear {name},\nGreetings For The Day...!\n\nMonthly Room rent has been calculated and find the below attached report.\nNote: We apologies if there is any mistakes in the report and please contact to admin for any changes.\n\nWith Best Regards,\nRoomate.com\n(A Product of ABC Technologies )")
        message.attach(Msg)

        #directory = r"C:\Users\Suhas\PycharmProjects\daya\dayaayb.pdf"
        with open(report, encoding = 'utf-8', errors = 'replace') as opened:
            openedfile = opened.read()
        attachedfile = MIMEApplication(openedfile, _subtype = "pdf", _encoder = encode_base64)
        attachedfile.add_header('content-disposition', 'attachment', filename = "Roomates"+str(mnth)+".pdf")
        message.attach(attachedfile)

        server = SMTP("smtp.gmail.com:587")
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(message['From'], message['To'], message.as_string())


        return True
    except Exception as E:
        return False

