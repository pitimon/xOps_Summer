from fastapi import FastAPI
from pydantic import BaseModel
from nameko.rpc import rpc
from nameko.standalone.rpc import ClusterRpcProxy

class Student(BaseModel):
    firstname:str
    lastname:str
    email:str

app = FastAPI()

broker_cfg = {'AMQP_URI': "amqp://guest:guest@rabbitmq"}

@app.post("/register/")
def api(student_item: Student):
    with ClusterRpcProxy(broker_cfg) as rpc:
        sid =rpc.student.insert(student_item.firstname, student_item.lastname, student_item.email)
        rpc.enroll.insert.call_async(sid, student_item.firstname, student_item.lastname)
        rpc.email.send.call_async(sid, student_item.firstname, student_item.lastname, student_item.email)

    print(sid)
    return {'results': 'registered'}
    