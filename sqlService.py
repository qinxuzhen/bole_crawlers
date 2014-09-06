 # -*- coding: utf-8 -*- 
import mysql.connector
from mysql.connector import errorcode

class sqlService:
    """ the class for operation of the database"""     
    def __init__(self,config):
        self.config = {
            'user':config['user'],
            'password':config['password'],
            'host':config['host'],
            'charset':'utf8'
            }
        try:
            self.cnx = mysql.connector.connect(**self.config)
            self.cursor = self.cnx.cursor(buffered=True)
            self.cursor.execute("set NAMES utf8")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
                exit(1)
            else:
                print(err)
                exit(1)
    
    def __del__(self):
        print("In __del__")
        try:
            self.cnx.close()
        except Exception:
            print("SQL connect free fail")
         
    def  connect_database(self, DB_NAME):
        try:
            self.cnx.database = DB_NAME
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(DB_NAME)
                self.cnx.database = DB_NAME
            else:
                print(err)
                exit(1)
                
    
    def query(self,query,data=None):
       
        self.cursor.execute(query,data)
        return self.cursor

    def update(self,query,data= None):
        self.cursor.execute(query,data)
        self.cnx.commit()
        
if __name__ == "__main__":
    config = {
        'user':user,
        'password':pwd,
        'host':'localhost',
    }
    DB_NAME = dbname
    info_class = '杭州'
    sql_service = sqlService(config)
    sql_service.connect_database(DB_NAME)
    sql_stat = ("INSERT INTO info_infoclass(className) VALUES ( %s )")
    sql_service.update(sql_stat,(info_class,))

