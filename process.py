# -*- coding: utf-8 -*-

import getPage
import bs4
import datetime
import sqlService
import dboperator

def ThreadUrl(hosts,sql_service):
    print ("In ThreadUrl")

    #create a infoOperator
    info_operator = dboperator.infoOperator(sql_service)

    for host in hosts:
        try:
            print (host)
            chunk = getPage.get(host, 3, 'utf-8')
        except Exception:
            print("get Page Error")
        #print chunk
        
        if chunk == None:
            continue
        # parse here then
        soup = bs4.BeautifulSoup(chunk)
        threadlist = soup.find('div', {"class": "main"})
        #if fail, then continue
        if threadlist == None:
            continue
        
        #the the urls in the first page
        for li in threadlist.findAll('li'):
            cursor = None
            try:
                head = li.h2.find('a',attrs = {'rel':'bookmark'})
                title = head.get_text()

                link = head['href']
                
                div = li.find('div',{'class':'info'})
                atts = div.findAll('a')
                info_area = atts[0].get_text()
                #print InfoArea
                info_class = atts[1].get_text()
                #print InfoClass
                info_local = atts[2].get_text()
                view_times = 0
                pub_date = datetime.datetime.now()
                content = getDetail(link)    
            except Exception:
                continue
            print (title,link, info_area,info_class,info_local) 

            #query the class
            class_id = info_operator.queryClass(info_class)
            if class_id == None:
               info_operator.insertClass(info_class)
               class_id = info_operator.queryClass(info_class)

            #query the area
            area_id = info_operator.queryArea(info_area)
            if area_id == None:
                info_operator.insertArea(info_area)
                area_id = info_operator.queryArea(info_area)

            #query the local
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
            
            '''
            #insert the relation of the location and info
            for local_id in local_ids:
                relation = (info_id,local_id)
                info_operator.insertInfoLocation(relation)
            '''
            #insert relation
            info_operator.insertRelation(info_id,location_id)
            
        
		#navigation in the bottom
        navigation = soup.find('div',attrs = {'class':'navigation'})
        next_page = navigation.find('span').next_sibling['href']
        print ('next_page:' + next_page)
        hosts.append(next_page)
             
def getDetail(link):
    print(link)
    try:
        chunk = getPage.get(link, 3, "utf-8")
    except Exception:
        print("Page Get Exception")
        
    content = ""            
    soup = bs4.BeautifulSoup(chunk)
    div = soup.find('div', attrs={"class":"context"})
    if div :
        for item in div.contents[2:-1]:
            content = content + str(item)
    return content       

    
if __name__ == "__main__":
    hosts = ['http://www.lovebanker.com/category/bank',
             'http://www.lovebanker.com/category/security',
             'http://www.lovebanker.com/category/funds',
             'http://www.lovebanker.com/category/trust',
             'http://www.lovebanker.com/category/insurance',
             'http://www.lovebanker.com/category/others']
    
    config = {
    	'user':user,
    	'password':pwd,
    	'host':'localhost',
    }
    DB_NAME = dbname
    sql_service = sqlService.sqlService(config)
    sql_service.connect_database(DB_NAME)
    ThreadUrl(hosts,sql_service)
    

