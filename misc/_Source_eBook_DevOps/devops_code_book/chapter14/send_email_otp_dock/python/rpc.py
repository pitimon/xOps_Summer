import smtplib
from email.message import EmailMessage
from nameko.rpc import rpc

def send_email(otp, email):
    msg = EmailMessage()
    text = "OTP สำหรับการลงทะเบียนนักศึกษาใหม่ของท่าน คือ " + str(otp) + ", OTP ของท่านจะหมดอายุใน 2 นาที"
    msg.set_content(text)

    msg['Subject'] = 'Register OTP'
    msg['To'] = email

    s = smtplib.SMTP("smtp_otp",25)
    s.ehlo()
    s.sendmail(from_addr = 'nuttachot@hotmail.com', to_addrs = email, msg = msg.as_string())
    s.quit()


class Email:
    name = "email_otp"

    @rpc
    def send(self, otp, email):
        send_email(otp, email)
        