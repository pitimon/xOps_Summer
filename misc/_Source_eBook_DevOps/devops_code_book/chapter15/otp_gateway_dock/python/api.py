from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from nameko.rpc import rpc
from nameko.standalone.rpc import ClusterRpcProxy
    
class Email(BaseModel):
    email:str
    
class EmailList(BaseModel):
    emails:List[str] = []
    
class Authen(BaseModel):
    email:str
    otp:str

app = FastAPI()

broker_cfg = {'AMQP_URI': "amqp://guest:guest@rabbitmq"}

@app.post("/getotp/")
def get_otp(email: Email):
    with ClusterRpcProxy(broker_cfg) as rpc:
        otp = rpc.otp.create(email.email)
        if otp != 0: 
           rpc.email_otp.send.call_async(otp, email.email)

    return {'results': str(otp)}
    
@app.post("/create_email_list/")
def create_email_list(email_list: EmailList):
    with ClusterRpcProxy(broker_cfg) as rpc:
        val = rpc.otp.create_email_list(email_list.emails)
  
    return {'results': val}
    
@app.post("/authen/")
def authen(authen: Authen):
    with ClusterRpcProxy(broker_cfg) as rpc:
        success = rpc.otp.authen(authen.email, authen.otp)
        if success == 1:
           rpc.otp.delete.call_async(authen.email)
           
    return {'results': success}
    