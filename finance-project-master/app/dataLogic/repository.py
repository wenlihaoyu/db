# -*- coding: utf-8 -*-
import sqlite3
import sys
import traceback
import urllib

#from model.order import *

class Repository(object):

    def create(self):
        pass

    def read(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass
    
    def save(self):
        pass

    
class MarketOrderRepository(Repository):
    TABLE = 'stock'
    LOCAL_TABLE_NAME=['stock_5min','stock_15min','stock_30min','stock_60min' ,'stock_month','stock_year']
    
    def __init__(self, database="db/finance.db", uid=None, passwd=None):
        self.database = database
        try:
            self.conn = sqlite3.connect(self.database)
            self.cursor = self.conn.cursor()
        except:
            self.conn.close()
            traceback.print_exc()
            sys.exit(1)

    def create(self, stock):
        try:
            self.stock=stock
            result=self.cursor.execute("SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name='stock';")
            if len(result)==0:
                self.cursor.execute('create table stock(symbol text primary key,name text ,market text ,source text,comment text)')
                self.conn.commit()
            sql = """insert into %s values('%s', '%s', '%s', %s, %s);""" %(TABLE, stock.symbol, stock.name,stock.market,stock.source,stock.comment)
            self.cursor.execute(sql)
        except:
            self.conn.close()
            traceback.print_exc()
            sys.exit(1)

    def read(self,period,begin,to):
        ###read the data from Yahoo
        self.stock.get_data(period,begin,to)
        pass
            
    def update(self):
        insert(self.stock.period)
        pass

    def delete(self, order):
        pass

    def save(self):
        try:
            self.conn.commit()
            self.conn.close()
        except:
            traceback.print_exc()
            sys.exit(1)
class stock:
    LOCAL_PERIOD=['5min','30min','60min' ,'day','month','year']
    LOCAL_SYMBOL=['Sina','Yahoo','Google','SOHU']
    def __init__(self,symbol,name,market,source,comment):
        self.symbol=symbol
        self.name=name
        self.matkert=market
        self.source=source
        self.comment=comment
        
    def get_data(self,period,begin,to):
        ##begin='2013-01-01'
        ##t0='2013-03-03'
        if period =='day':
            self.period='d'
        def get_from_url(symbol,period,source,begin,to):
            def get_time(t):
                if t==None or t=="":
                  t_year=""
                  t_month=""
                  t_day=""
                else:
                  t_year=str(int(t[0:4]))
                  t_month=str(int(t[5:7])-1)
                  t_day=str(int(t[8:10]))
                return list([t_year,t_month,t_day])
            begin_time=get_time(begin)
            to_time=get_time(to)  
            if source == 'Yahoo':
            #url='http://finance.yahoo.com/d/quotes.csv?s=%s&f='
                url='http://ichart.yahoo.com/table.csv?s=%s&a=%s&b=%s&c=%s&d=%s&e=%s&f=%s&g=%s&ignore=.csv'%(symbol,begin_time[1],begin_time[2],begin_time[0],to_time[1],to_time[2],to_time[0],period)
                response=urllib.urlopen(url)
                response=response.read()
                data=str(response)
                data=data.split('\n')
                data=[da.split(',') for da in data]
                data=data[:len(data)-1]
                return data
            else :
                return ''
        self.period=get_from_url(self.symbol,self.period,self.source,begin,to)   
#参数

#s – 股票名称

#a – 起始时间，#月

#b – 起始时间，日

#c – 起始时间，年

#d – 结束时间，月

#e – 结束时间，日

#f – 结束时间，年
#g – 时间周期。Example: g=w, 表示周期是’周’。d->’日’(day),w->’周’(week)，m->’月’(mouth)

    
