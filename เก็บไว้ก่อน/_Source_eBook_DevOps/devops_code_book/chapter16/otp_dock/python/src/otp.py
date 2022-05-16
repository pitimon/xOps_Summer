import math, random 
from validate_email import validate_email
import redis

import os
from dotenv import load_dotenv 

load_dotenv('./.env')
email_list_key = os.getenv("email_list_key")

def connect():
    redisConnect = redis.Redis(host='otp_redis', port=6379)
    return redisConnect

redisConnect = connect()

def generate_otp():
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

def get_email_list_key():
    return email_list_key