# import sqlite3
#
# from encrept import *
# class my_database:
#     def __init__(self):
#         self.db = sqlite3.connect('authetication.db')
#     def table(self):
#         conn = self.db.cursor()
#         # conn.execute("CREATE TABLE users (ID INTEGER NOT NULL AUTOINCREMENT PRIMARY KEY,F_from VARCHAR(150) NOT NULL ,l_to VARCHAR(200) NOT NULL,authetication NOT NULL,number_scan VARCHAR(50) NOT NULL)")
#
#         conn.execute("CREATE TABLE user(id int NOT NULL PRIMARY KEY,f_date  NOT NULL,l_date NOT NULL,num_scan int NOT NULL)")
#         p
#
#     def insert_values(self,id,f_date,l_date,num_scan):
#         conn = self.db.cursor()
#         entity = (id,f_date,l_date,num_scan)
#         conn.execute('INSERT INTO user (id, f_date,l_date,num_scan) VALUES (?,?,?,?)', entity)
#         self.db.commit()
#
#     def read_db(self,id):
#         conn = self.db.cursor()
#         res = conn.execute(f"SELECT * FROM user WHERE id={id}")
#         self.data = res.fetchone()
#
#
import sqlite3
def scan_m(id):
    db = sqlite3.connect('authetication.db')
    conn = db.cursor()
    r = conn.execute(f"SELECT * FROM user WHERE id={id}")
    d = r.fetchone()
    res = conn.execute(f"UPDATE user SET num_scan={d[3]-1} WHERE id ={id}")
    db.commit()
    fetch = conn.execute(f"SELECT * FROM user WHERE id={id}")
    fetchs = fetch.fetchone()

    
    return fetchs[3]
#
# scan_m(11)


# my = my_database()
# my.scan(8)
# my.table()
# my.insert_values(5,'17/3/2020','19/3/2020',3)
# my.insert_values(6,'17/3/2020','20/3/2020',4)
# my.insert_values(12,'17/3/2020','25/3/2020',6)
# my.read_db(10)

