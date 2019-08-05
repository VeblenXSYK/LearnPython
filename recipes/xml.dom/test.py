#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf8') 
from xml.dom import minidom
import os
import logging
import traceback


class CSysConfig:

	"""系统全部配置信息"""

	def __init__(self):
		pass

	def LoadConfig(self, filepath = ''):

		"""加载配置文件：成功返回True，否则False。"""

		self.filepath = filepath
		
		try:
			XmlFile = open(filepath, 'rb')
			XmlData = XmlFile.read()
			XmlFile.close()
			
			Doc = minidom.parseString(XmlData)
			collection = Doc.documentElement

			# 从集合中获取所有的电影
			movies = collection.getElementsByTagName('movie')
			
			# 打印每部电影的详细信息
			for movie in movies:
				print "*****Title: %s*****" % movie.getAttribute('title')
				type = movie.getElementsByTagName('type')[0]
				print "Type: %s" % type.childNodes[0].data
				
				description = movie.getElementsByTagName('description')[0]
				print "Description: %s" % description.childNodes[0].data
				print "" 
		except:
			logging.error('解析配置文件异常 : %s' % traceback.format_exc())
			return False

		return True	
		
if __name__ == '__main__':
		
	sysconf = CSysConfig()
	sysconf.LoadConfig("config.xml")
	