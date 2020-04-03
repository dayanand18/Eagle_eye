import sqlite3
import os
from datetime import datetime

class rommate_db:

    def __init__(self):
        self.db = sqlite3.connect('Roomates.db')


    def create_roomates_table(self):
        try:
            query = "CREATE TABLE roomates(user_mail text PRIMARY KEY NOT NULL,full_name VARCHAR(200) NOT NULL, company_name VARCHAR(150),password text NOT NULL,user_role INTEGER NOT NULL, last_login VARCHAR(200) NOT NULL,user_status INTEGER DEFAULT 0 NOT NULL)"
            self.db.execute(query)
            self.insert_user('ABCD Tech','abcd@technologies.com','ABCD Technologies','abcdcbA@4321',urole=1,u_status=1)
        except Exception as E:
            print(E)
    # def create_roomates_table(self):
    #     try:
    #         query = "CREATE TABLE roomates(user_mail text PRIMARY KEY NOT NULL,full_name VARCHAR(200) NOT NULL, company_name VARCHAR(150),password text NOT NULL,user_role INTEGER NOT NULL, last_login VARCHAR(200) NOT NULL,user_status INTEGER DEFAULT 0 NOT NULL)"
    #         self.db.execute(query)
    #     except Exception as E:
    #         print(E)
    def insert_user(self,full_name,email,company,password,urole=3,u_status=0):
        try:
            query = "INSERT or IGNORE INTO roomates(user_mail,full_name,company_name,password,user_role,last_login,user_status) VALUES(?,?,?,?,?,?,?)"
            last_login = str(datetime.now()).split('.')[0]
            parameters = (email,full_name,company,password,urole,last_login,u_status)
            self.db.cursor()
            self.db.execute(query,parameters)
            self.db.commit()
            return True
        except Exception as errr:
            if str(errr).__contains__('no such table: roomates'):
                self.create_roomates_table()
                self.insert_user(full_name,email,company,password)
            return False
        except:
            return False

    def get_emails(self):
        usr_maial_lst = []
        try:
            query = f"SELECT user_mail FROM roomates"
            self.db.cursor()
            self.data = self.db.execute(query)
            usr_maial_lst = self.data.fetchall()
        except:
            return usr_maial_lst
        finally:
            return usr_maial_lst

    def search_user(self,mail):
        try:
            query = f"SELECT * FROM roomates WHERE user_mail='{mail}'"
            self.db.cursor()
            self.data = self.db.execute(query)
            return self.data.fetchall()
        except Exception as errr:
            if str(errr).__contains__('no such table: roomates'):
                self.create_roomates_table()
            return []
        except:
            self.db.rollback()


    def update_user(self,mail,col_name,val):
        try:
            query = f"UPDATE roomates SET {col_name}='{val}' WHERE user_mail='{mail}'"
            self.db.cursor()
            self.db.execute(query)
            self.db.commit()
        except Exception as errr:
            print (errr)
            if str(errr).__contains__('no such table: roomates'):
                self.create_roomates_table()
            return False
        except:
            self.db.rollback()

    def update_user_status(self,mail,status):
        try:
            query = f"UPDATE roomates SET user_status={status} WHERE user_mail='{mail}'"
            self.db.cursor()
            self.db.execute(query)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False


    def delete_box(self,user):
        try:
            query = f"DELETE FROM roomates WHERE user_mail='{user}'"
            self.db.cursor()
            self.db.execute(query)
            self.db.commit()
            return True
        except:
            return False

    def delete_db(self):
        try:
            query = "DROP TABLE roomates"
            self.db.execute(query)
            os.remove('Roomates.db')
        except:
            pass

    def pdf_generated(self):
        try:

            query = "SELECT user_mail, full_name FROM roomates"
            db = sqlite3.connect('Roomates.db')
            db.cursor()
            data = db.execute(query)
            d = data.fetchall()
            # print(d)
            return d
        except:
            return False
# query = "SELECT user_mail, full_name FROM roomates"
# db = sqlite3.connect('Roomates.db')
# db.cursor()
# data = db.execute(query)
# d = data.fetchall()
# print(d)

# mail ='shiva.vh3@gmail.com'
# query = f"SELECT * FROM roomates WHERE user_mail"
# db = sqlite3.connect('Roomates.db')
# db.cursor()
# data = db.execute(query)
# print(data.fetchall())

# ob = rommate_db()
#
# ob.pdf_generated()
# query = "ALTER TABLE roomates ADD payment INTEGER DEFAULT 0 NOT NULL"
# Last_login = str(datetime.now()).split('.')[0]
# self.dbr.update_user(user,'last_login',str(Last_login))

# query = "SELECT * FROM roomates"
# # # # lst = []
# #query = "SELECT user_mail FROM roomates"
# db = sqlite3.connect('Roomates.db')
# db.cursor()
# data = db.execute(query)
# print(data.fetchall())
# for usr in d:
#     print(usr[0])


# a = rommate_db()
# # #a.delete_db()
#print(a.update_user_status('dayaayb@gmail.com',1))
#print(a.search_user('shiva.vh3@gmail.com'))


# query = "UPDATE roomates SET user_role=1 WHERE user_mail='daya.ba007@gmail.com'"
#
# db = sqlite3.connect('Roomates.db')
# db.cursor()
# db.execute(query)
# db.commit()


# query = "DELETE FROM roomates WHERE user_mail='shiva.vh3@gmail.com'"
#
# db = sqlite3.connect('Roomates.db')
# db.cursor()
# db.execute(query)
# db.commit()

