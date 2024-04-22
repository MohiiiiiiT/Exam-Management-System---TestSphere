from mysql.connector import *
def getConn():
    return connect(host='localhost',user='root',password='')