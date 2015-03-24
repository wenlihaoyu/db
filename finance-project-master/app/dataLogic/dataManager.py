# -*- coding: utf-8 -*-
import urllib
import sqlite3
class DataManager(object):

    def create(self):
        pass
    
    def update(self):
        pass

    def delete(self):
        pass


class StockDataManager:
    LOCAL_TABLE_NAME=['stock_5min','stock_15min','stock_30min','stock_60min' ,'stock_month','stock_year']
    LOCAL_PERIOD=['5min','30min','60min' ,'month','year']
    LOCAL_SYMBOL=['Sina','Yahoo','Google','SOHU']
    #def __init__(self):
     #   self.falg=True
    def Create(self, symbol, name, market, source, comment,db_name):
	conn=sqlite3.connect(db_name)
        c= conn.cursor()
        x=c.execute("SELECT tbl_name FROM sqlite_master WHERE type='table' and tbl_name='stock';")
        result=x.fetchall()
        if len(result)==0:
        ## 创建表
            c.execute('create table '+ 'stock'+'(symbol text primary key,name text ,market text ,source text,comment text)')
            conn.commit()
        ###插入到基本表中
        c.execute('insert into '+'stock'+ ' values('+"'"+symbol+"','"+ name+"','"+market+"','"+source+"','"+comment+"')")
        conn.commit()
        conn.close()

    def Update(self, symbol, period, begin,to, dataset,source,db_name):
        ##将生成的数据更新到表中
        conn=sqlite3.connect(db_name)
        c = conn.cursor()
        x=c.execute("select distinct source from stock where symbol='"+symbol+"' and source='"+source+"';" )
        result=x.fetchall()
        conn.close()
        if period not in self.LOCALj_PERIOD:
            print '当前period'+period+'不正确'
        elif len(result)==0:
            print '不能从当前的source:'+source+'获取数据'
        
        else:
            data=self.__get_data_from__(source,symbol,period,begin,to)
            self.__insert_data__(data,period)
    
    def __get_data_from__(source,symbol,period,begin,to):
        LOCAL_URL={}
        LOCAL_URL['Sina']={'5min':"",
                           '15min':"",
                           '30min':"",
                            "60min":"",
                            'day':"",
                            'month':"",
                            'year':""
                                }
        LOCAL_URL['Yahoo']={'5min':"",
                            '15min':"",
                            '30min':"",
                            "60min":"",
                            'day':"http://finance.yahoo.com/d/quotes.csv?s=",
                            'month':"",
                            'year':""
                              }
        LOCAL_URL['Google']={'5min':"",
                             '15min':"",
                             '30min':"",
                             "60min":"",
                             'day':"",
                             'month':"",
                             'year':""
                              }
        LOCAL_URL['SOHU']={'5min':"",
                       '15min':"",
                       '30min':"",
                       "60min":"",
                       'day':"",
                       'month':"",
                       'year':""
                       }
    
        for key in LOCAL_URL:
           if key ==source:
                for next_key in LOCAL_URL[key]:
                    if next_key == period:
                       url=LOCAL_URL[key][next_key]
                       break
    
        #url="http://table.finance.yahoo.com/table.csv?s="+name
        response=urllib.request.urlopen(url)
        response=response.read()
        data=str(response,"utf-8")
        data=data.split('\n')
        data=[da.split(',') for da in data]
        data=data[1:]
        data=data[:len(data)-1]
        return(data)
        
    def __insert_data__(data,period):
        conn=sqlite3.connect(db_name)
        for i in range(len(LOCAL_TABLE_NAME)):
            if LOCAL_PERIOD[i]==period:
                table_names=LOCAL_TABLE_NAME[i]
                break
        c = conn.cursor()
        String=''
        for i in range(data):
            if i != len(data)-1:
                String+=str(data[i])+','
            else:
                String+=str(data[i])
        String="insert into "+ table_names + " values (" + String +")"
        c.execute(String)
        conn.commit()
        conn.close()
    def Delete(self, symbol, period):
        if period not in self.LOCAL_PERIOD:
            print "当前period："+ period+'错误，无法完成删除操作'
        for i in local_period:
            if period==local_period[i]:
                conn=sqlite3.connect(db_name)
                c = conn.cursor()
                c.execute("delete from "+ local_table_name[i] + "where symbol='" + symbol )
                conn.commit()
                conn.close()
                print "删除操作成功！"
                break
    
    



def DataManagerInstance(instance):
    global gdataManager
    try:
        gdataManager
    except:
        if instance == 'stock':
            gdataManager = StockDataManager()
    return gdataManager

