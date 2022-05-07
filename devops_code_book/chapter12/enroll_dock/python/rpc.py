import MySQLdb
from nameko.rpc import rpc

def connect():
    DBconnect = MySQLdb.connect(host='db',
                     user='devops',
                     passwd='devops101',
                     db='devops_db',
                     port=3306)
    return DBconnect

def insert(id, firstname, lastname, subjectid, term, year):
    DBconnect = connect()
    cur = DBconnect.cursor()
    cur.execute("INSERT INTO enroll (id, name, subjectid, term, year) VALUES (%s, %s, %s, %s, %s);", (id, firstname + ' ' + lastname, subjectid, term, year))
    id = cur.lastrowid
    DBconnect.commit()
    DBconnect.close()
    return id

class Service:
    name = "enroll"

    @rpc
    def insert(self, id, firstname, lastname):
        result = insert(id, firstname, lastname, '081102', 1, 2563)
        result = insert(id, firstname, lastname, '520101', 1, 2563)
        result = insert(id, firstname, lastname, '511100', 1, 2563)
        result = insert(id, firstname, lastname, '517121', 1, 2563)
        return result
        