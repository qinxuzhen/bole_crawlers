# -*- coding: utf-8 -*-

import getPage
import bs4

if __name__ == '__main__':
    req = 'http://www.lovebanker.com/category/bank'
    str = getPage.get(req,3,'utf-8') 
    soup = bs4.BeautifulSoup(str)
    threadlist = soup.find('div', {"class": "main"})    
    for li in threadlist.findAll('li'):
        # location
        head = li.h2.find('a', attrs={'rel':'bookmark'})
        title = head.get_text()
        detail_page = head['href']
        div = li.find('div', {'class':'info'})
        atts = div.findAll('a')
        info_area = atts[0].get_text()
        # print InfoArea
        info_class = atts[1].get_text()
        # print InfoClass
        info_local = atts[2].get_text()
        
        print (title,detail_page,info_area,info_class,info_local)
        '''
        location =  [item.get_text() for item in li.h2.findAll('a',attrs={"rel": "tag"})]
        print location[0].encode('utf-8')
        print li.h2.find('a',attrs = {'rel':'bookmark'})['href']
        '''
        
    req = 'http://www.lovebanker.com/security/20140813/12319.html'
    str = getPage.get(req,3,'utf-8') 
    soup = bs4.BeautifulSoup(str)
    div = soup.find('div',attrs={"class":"context"})
    if div:
        content = ""
        for parag in div.findAll('p'):
            content = content + parag.get_text()
        print (content)
    
