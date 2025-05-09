#Trabajo de sqlite
import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()

con = sqlite3.connect(dataBaseManager.database)
cur =con.cursor()
cur.execute("select * from Materias;")
cur.execute

table_list =list = cur.fetchall()

for row in table_list:
    print(row)


    con.close() 

    dataBaseManager = DataBaseManager()
db_file = 'C:/Users/CompuAula 03/Documents/gera/testing.db'
