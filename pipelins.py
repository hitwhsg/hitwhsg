# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy.crawler import Settings as settings
class SgPipeline(object):

    def __init__(self):

        dbargs = dict(
            host = 'your host' ,
            db = 'crawed',
            user = 'user_name', #replace with you user name
            passwd = 'user_password', # replace with you password
            charset = 'utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
            )    
        self.dbpool = adbapi.ConnectionPool('MySQLdb',**dbargs)


    '''
    The default pipeline invoke function
    '''
        def process_item(self, item,spider):
            res = self.dbpool.runInteraction(self.insert_into_table,item)
                return item

        def insert_into_table(self,conn,item):
                conn.execute('insert into info(title,url,body) values(%s,%s,%s)', (item['title'],item['url'],item['body']))

'''
class SgPipeline(object):
    def __init__(self):
        self.file = codecs.open('aa.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item
    def spider_closed(self,spider):
        self.file.close()'''
