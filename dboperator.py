#-*- coding: utf-8 -*-

import sqlService
import datetime
import time

class infoOperator():
    """the sql statement of db"""
    def __init__(self,sql_service):
        self.sql_service = sql_service

    def insertClass(self,info_class):
        sql_stat = ("INSERT INTO info_infoclass ( className )  VALUES ( %s )")
        print(sql_stat,info_class)
        try:
            self.sql_service.update(sql_stat,(info_class,))
        except Exception:
            print("MySQL Error: insertClass:",sql_stat,info_class)
            return False
        return True

    def queryClass(self,info_class):
        sql_stat = ("SELECT * FROM info_infoclass WHERE className = %s " )
        print(sql_stat,info_class)
        result = None
        try:
            cursor = self.sql_service.query(sql_stat,(info_class,))
            result = cursor.fetchone()
        except Exception:
            print ("MySQL Error: queryClass:",sql_stat, info_class)
        if result:
            return result[0]
        return None
        
    
    def insertArea(self,info_area):
        sql_stat = ("INSERT INTO info_infoarea ( areaName )  VALUES ( %s )")
        print(sql_stat,info_area)
        try:
            self.sql_service.update(sql_stat,(info_area,))
        except Exception:
            print("MySQL Error: insertArea:",sql_stat,info_area)
            return False
        return True

    def queryArea(self,info_area):
        sql_stat = ("SELECT * FROM info_infoarea WHERE areaName = %s " )
        print(sql_stat,info_area)
        result = None
        try:
            cursor = self.sql_service.query(sql_stat,(info_area,))
            if cursor:
                result = cursor.fetchone()
        except Exception:
            print ("MySQL Error: queryArea:",sql_stat, info_area)
        if result:
            return result[0]
        return None

        
    def insertLocation(self,location):
        sql_stat = ("INSERT INTO info_infolocation (location )  VALUES ( %s )")
        print(sql_stat,location)
        try:
            self.sql_service.update(sql_stat,(location,))
        except Exception:
            print("MySQL Error: insertLocation:",sql_stat,location)
            return False
        return True

    def queryLocation(self,location):
        sql_stat = ("SELECT * FROM info_infolocation WHERE location = %s " )
        print(sql_stat,location)
        result = None
        try:
            cursor = self.sql_service.query(sql_stat,(location,))
            result = cursor.fetchone()
        except Exception:
            print ("MySQL Error: queryLocation:",sql_stat, location)
        if result:
            return result[0]
        return None


    def insertInfo(self,info):
        sql_stat = ("INSERT INTO info_info (title,content,view_times,pub_date,info_area_id,info_class_id ) VALUES ( %s, %s, %s, %s, %s, %s )" )
        print(sql_stat,info)
        try:
            self.sql_service.update(sql_stat,info)
        except Exception:
            print("MySQL Error: insertInfo:",sql_stat,info)
            return False
        return True

    def queryInfo(self,info):
        sql_stat = ("SELECT * FROM info_info WHERE title = %s and info_area_id = %s and info_class_id = %s and pub_date = %s " )
        print(sql_stat,info)
        result = None
        try:
            cursor = self.sql_service.query(sql_stat,info)
            result = cursor.fetchone()
        except Exception:
            print ("MySQL Error: queryInfo:",sql_stat, info)
        if result:
            return result[0]
        return None


    def insertRelation(self,info_id,location_id):
        sql_stat = ("INSERT INTO info_info_info_location( info_id,infolocation_id)  VALUES ( %s, %s )")
        print(sql_stat,info_id,location_id)
        try:
            self.sql_service.update(sql_stat,(info_id,location_id,))
        except Exception:
            print("MySQL Error: insertRelation:",sql_stat,info_id,location_id)
            return False
        return True

    def queryRelation(self,info_id,location_id):
        sql_stat = ("SELECT * FROM info_info_info_location WHERE info_id = %s and infolocation_id = %s " )
        print(sql_stat,info_id,location_id)
        result = None
        try:
            cursor = self.sql_service.query(sql_stat,(info_id,location_id,))
            result = cursor.fetchone()
        except Exception:
            print ("MySQL Error: queryRelation:",sql_stat, info_id,location_id)
        if result:
            return result[0]
        return None
   

'''
    def insertArea(self,area_name):
        
        return  self.insertItem('info_infoclass','className',(class_name,))

    def queryClass(self,class_name):
        condition = 'className = %s '
        result =self.queryItem('info_infoclass',condition,(class_name,))
        if result:
            return result[0]
        return None

    def insertArea(self,area_name):
        return self.insertItem('info_infoarea','areaName',(area_name,))

    def queryArea(self,area_name):
        condition = 'areaName = %s '
        result = self.queryItem('info_infoarea',condition,(area_name,))
        if result:
            return result[0]
        return None
    
    def queryLocal(self,local_list):
        local_ids = []
        condition = 'location = %s '
        for local in local_list:
            result = self.queryItem('info_infolocation',condition,(local,))
            if result:
                local_ids.append(result[0])
        if local_ids == []:
            return None
        return local_ids

    def insertLocal(self,local_list):
        for local in local_list:
            status = self.insertItem('info_infolocation','location',(local,))
            if status == False:
                return False
        return True

    def insertInfo(self,info_item):
        columns = 'title,content,view_times,pub_date,info_area_id,info_class_id'
        values = ' %s,%s,%s,%s,%s,%s '
        result = self.insertItem('info_info',columns,info_item,values)
        return result

    def queryInfo(self,info_item):
        condition = 'title = %s and info_area_id = %s and info_class_id = %s and pub_date = %s'
        result = self.queryItem('info_info',condition,info_item)
        if result:
            return result[0]
        return None

    def insertInfoLocation(self,relation):
        columns = 'info_id,infolocation_id'
        values = '%s, %s '
        result = self.insertItem('info_info_info_location',columns,relation,values)
        return result

    def queryInfoLocation(self,relation):
        condition = 'info_id = %s and infolocation_id = %s'
        result = self.queryItem('info_info_info_location',condition,relation)
        if result:
            return result[0]
        return None
    '''

    
if __name__ == '__main__':
    config = {
        'user':user,
        'password':pwd,
        'host':'localhost',
    }
    DB_NAME = dbname
    sql_service = sqlService.sqlService(config)
    sql_service.connect_database(DB_NAME)
    info_operator = infoOperator(sql_service) 
    title = '浦发硅谷银行招聘市场部实习生'
    link = 'http://www.lovebanker.com/bank/20140801/12149.html'
    info_area = '银行'
    info_class = '实习'
    info_local = '上海'
    view_times = 0
    pub_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    content = "1.负责审查总行各管理条线制定、修订的各项规章制度"

    
    #query the class
    
    class_id = info_operator.queryClass(info_class)
    print(class_id)
    if class_id == None:
        info_operator.insertClass(info_class)
        class_id = info_operator.queryClass(info_class)
    print(class_id)
    
    #query the area
    print(info_area)
    area_id = info_operator.queryArea(info_area)
    print(area_id)
    if area_id == None:
        info_operator.insertArea(info_area)
        area_id = info_operator.queryArea(info_area)
    '''
    #query the local
    location_list = []
    for location in info_local:
        print("in loop location",location)
        local_id = info_operator.queryLocation(location)
        if local_id:
            location_list.append(local_id)
        else:
            info_operator.insertLocation(location)
            local_id = info_operator.queryLocation(location)
            location_list.append(local_id)
    print(location_list)
    '''
    #query the location
    location_id = info_operator.queryLocation(info_local)
    print(location_id)
    if location_id == None:
        info_operator.insertLocation(info_local)
        location_id = info_operator.queryLocation(info_local)

    #insert info
    info_item = (title,content,view_times,pub_date,area_id,class_id)
    info_operator.insertInfo(info_item)
    info_item = (title,area_id,class_id,pub_date)
    info_id = info_operator.queryInfo(info_item)

    #insert the relation of the location and info
    '''
    for local_id in local_ids:
        relation = (info_id,local_id)
        info_operator.insertInfoLocation(relation)
    '''







    


