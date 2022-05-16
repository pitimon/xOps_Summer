from nameko.rpc import rpc
from datetime import timedelta

from src import otp
import os
from dotenv import load_dotenv

load_dotenv('.env')
email_list_key = os.getenv("email_list_key")

redisConnect = otp.connect()

class OTPService:
    name = "otp"

    @rpc
    def create(self, email):
        otp_number = 0
        if otp.exist_email(email):
            otp_number = otp.generate_otp()
            redisConnect.setex(email, timedelta(minutes=2), str(otp_number))
        return otp_number

    @rpc
    def delete(self, email):
        success = 0
        if otp.exist_email(email):
            redisConnect.srem(email_list_key, email) 
            redisConnect.delete(email)
            success = 1

        return success

    @rpc
    def create_email_list(self, emails):
        val = {}
        setExpire = False
        for email in emails:
            if otp.val_email(email) and not otp.exist_email(email): 
                redisConnect.sadd(email_list_key, email)
                val[email] = 'done'
                setExpire = True
            else: 
                val[email] = 'error'
            
        if setExpire: 
           redisConnect.expire(email_list_key, 60*60*24*30)
           
        return val

    @rpc
    def authen(self, email, otp_number):
        success = 0
        if otp.exist_key(email):
            test = redisConnect.get(email)
            otp_number = bytes(otp_number, 'utf-8')
            if test == otp_number:
               success = 1
               
        return success
