import sqlService
from process import ThreadUrl

if __name__ =="__main__":
    """ The entry of the crawler """
    #get the configure of the crawler
    config_file = open('/home/property/dbconfig','r')
    config = {}
    for line in config_file:
        line_list = list(line.split(':'))
        config[line_list[0]] = line_list[1]
    config_file.close()

    print(config)
    
    #connect to the database
    sql_service = sqlService.sqlService(config)
    sql_service.connect_database(config['database'])
    
    
    #different web has different sparser
    #process.process(hosts,sql_service)
    hosts = ['http://www.lovebanker.com/category/bank',
            'http://www.lovebanker.com/category/security',
            'http://www.lovebanker.com/category/funds',
            'http://www.lovebanker.com/category/trust',
            'http://www.lovebanker.com/category/insurance',
            'http://www.lovebanker.com/category/others']

    ThreadUrl(hosts,sql_service)    
