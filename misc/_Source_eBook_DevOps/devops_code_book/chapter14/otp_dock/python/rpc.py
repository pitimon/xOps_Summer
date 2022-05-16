from nameko.rpc import rpc
import math, random 
from datetime import timedelta
from validate_email import validate_email
import redis

email_list_key = 'register_email'

def connect():
    redisConnect = redis.Redis(host='otp_redis', port=6379)
    return redisConnect

redisConnect = connect()

def generate_otp(email):
    digits = "0123456789"
    otp = ""

    for i in range(6) :
        otp += digits[math.floor(random.random() * 10)]

    return otp

def exist_key(email):
    data = redisConnect.exists(email)
    if data == 1:
        exist = True
    else:
        exist = False

    return exist
    
def exist_email(email):
    set_email = redisConnect.smembers(email_list_key)
    email = bytes(email, 'utf-8')
    if email in set_email:
        exist = True
    else:
        exist = False

    return exist

def val_email(email):
    is_valid = validate_email(email)
    return is_valid

class OTPService:
    name = "otp"

    @rpc
    def create(self, email):
        otp = 0
        if exist_email(email):
            otp = generate_otp(email)
            redisConnect.setex(email, timedelta(minutes=3), str(otp))
        return otp

    @rpc
    def delete(self, email):
        success = 0
        if exist_email(email):
            redisConnect.srem(email_list_key, email)
            success = 1

        return success

    @rpc
    def create_email_list(self, emails):
        val = {}
        setExpire = False
        for email in emails:
            if val_email(email) and not exist_email(email): 
                redisConnect.sadd(email_list_key, email)
                val[email] = 'done'
                setExpire = True
            else:
                val[email] = 'error'

        if setExpire:
           redisConnect.expire(email_list_key, 60*60*24*30)

        return val

    @rpc
    def authen(self, email, otp):
        success = 0
        if exist_key(email):
            test = redisConnect.get(email)
            otp = bytes(otp, 'utf-8')
            if test == otp:
               success = 1
               
        return success
        