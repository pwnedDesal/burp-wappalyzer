#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#http://zetcode.com/db/sqlitepythontutorial/
import base64
import sqlite3 as lite
import time
import sys
class DBconnect:
    def __init__(self,dbpath,tableName='test'):
        self.tableName=tableName
        try:
            self.con = lite.connect(dbpath)
            self.cur = self.con.cursor()
            #print('ok')
        except lite.Error:
            print("Error {}:".format('hotdoy'))
            sys.exit(1)
        finally:
            if self.con:
                print('___')
                #self.con.close()
        if (self.isExistTable('scrap') == False):
            print('scrap table does not exist. Creating table...')
            self.createScrapTable()
    def version(self,statement):
        self.cur.execute('SELECT SQLITE_VERSION()')
        self.data = self.cur.fetchone()[0]
        return self.data
    def isExistRecord(self,url,wappalyer_scrap):
        self.cur.execute('SELECT * FROM scrap where url=? and scrapData=?',(url, wappalyer_scrap))
        self.data=self.cur.fetchone()
        if self.data==None:
            print('record does not exist')
            print(self.data)
            return False
        else:
            return True
    def isExistTable(self,table):
        data=self.cur.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?",(table,))
        if data.fetchone()[0]==1:
            return True
        else:
            return False
    def insertRecord(self,url,wappalyer_scrap,host,timestamp):
        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("INSERT INTO scrap(url,scrapData,Host,STime) VALUES(?,?,?,?)",(url, wappalyer_scrap,host,timestamp))
    def createScrapTable(self):
        with self.con:
            self.cur=self.con.cursor()
            result=self.cur.execute("CREATE TABLE scrap(id INTEGER PRIMARY KEY, url TEXT, scrapData TEXT,Host TEXT,STime TEXT)")
        return result
    def testScriptSelect(self):
        self.cur.execute("select * from scrap")
        rows=self.cur.fetchall()
        if len(rows)==0:
            print('notn')
        for row in rows:
            print(row['url'])
    def testScriptCreate(self):
        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("CREATE TABLE scrap(id INT, url TEXT, scrapData TEXT)")
            self.cur.execute("INSERT INTO scrap VALUES(1,'DDD','DDDD')")
            self.cur.execute("INSERT INTO scrap VALUES(2,'DD22D','DD22DD')")
    def closeDB(self):
        self.con.close()


def main():
    thefuck = DBconnect("sqlite\\test.db")
    message_bytes = base64.b64decode(sys.argv[2]).decode('ascii')
    if not thefuck.isExistTable('scrap'):
        thefuck.createScrapTable()
    if thefuck.isExistRecord(sys.argv[1], message_bytes) == False:
        ts = time.time()
        try:
            thefuck.insertRecord(sys.argv[1], message_bytes, sys.argv[3], ts)  # url,wappalyer_scrap,host,timestamp
        except:
            print('err')
    else:
        print('record exists,not saved')
    thefuck.closeDB()

if __name__ == "__main__":
    main()
