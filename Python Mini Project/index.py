import os
from connection_provider import *

conn=getConn()
querryWriter=conn.cursor()
querry="create database if not exists qemspython"
querryWriter.execute(querry)
querry="create table if not exists qemspython.teacherrecord(t_id varchar(20),name varchar(50),username varchar(50),password varchar(50))"
querryWriter.execute(querry)
querry="create table if not exists qemspython.studentrecord(s_id varchar(20),name varchar(50),username varchar(50),password varchar(50))"
querryWriter.execute(querry)
conn.commit()
os.system("python main.py")
