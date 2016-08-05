# -*- coding:utf-8 -*-
import requests as rr
import re
import json
import sqlite3
from contextlib import closing
import SpiderOrm
import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

class BingPicSpider():
	def __init__(self,idx):
		self.bingTodayPicApi = 'http://www.bing.com/HPImageArchive.aspx?format=js&idx=%d&n=1&nc=1'%idx
		self.integratedInfo = ()
		self.raw_api = self.apply_api()

	def apply_api(self):
		json_str = rr.get(self.bingTodayPicApi).text
		self.raw_api = json.loads(json_str).get('images')[0]
		return self.raw_api

	def extractIntegratedInfo(self):
		title = self.raw_api.get('copyright')
		picurl = self.raw_api.get('url')
		picbinary = rr.get(picurl).content
		date = self.raw_api.get('enddate')

		self.integratedInfo = (title,picurl,picbinary,date)
		return self.integratedInfo

def addPicInfoToDB(db,idx=0):
	BingPic = SpiderOrm.BingPic
	title,picurl,picbinary,date = BingPicSpider(idx).extractIntegratedInfo()
	logging.debug(" title:%s\n url:%s\n date:%s \n"%(title,picurl,date))
	bp = BingPic(title=title,picurl=picurl,picbinary=picbinary,date=date)
	db.add(bp)
	return bp

def addTodayPicToDB():
	db = SpiderOrm.BingPicDB()
	if db.initFlag and db.getLatest().date == str(datetime.date.today().strftime('%Y%m%d')):#如果最近一条是今天的,就说明重复添加
		raise Exception("Today's pic has already in db error!")
	else:
		return addPicInfoToDB(db)

def addUninsertedPicToDB():
	db = SpiderOrm.BingPicDB()

	uninsertedIndexs = list(db.findUnInsertedDayIndex())
	if len(uninsertedIndexs) == 0:
		raise Exception('All inserted error!')

	for idx in uninsertedIndexs:
		return addPicInfoToDB(db,idx)

if __name__=="__main__":
	#b = BingPicSpider(0)
	#integratedInfo = b.extractIntegratedInfo()
	#print(integratedInfo[1])
	addUninsertedPicToDB()