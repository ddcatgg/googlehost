#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 谷歌host修改脚本
# author pop<hipop#126.com>
# date 01/05/015
#
# 【使用说明】
# 请确保在当“前用户对host可写”前提下使用；
# AT一下，每天运行一次更健康；
# 本品禁止食用、拆解或投入火中；
# 小学生请在监护人陪同下一起使用；
# 孕妇慎用。
import sys, os
import urllib, urllib2, re

URL = 'http://www.360kb.com/kb/2_122.html'

PATT_CONTENT = r'#google hosts (\d{4})\.\d{2}\.\d{2}.*#google hosts \1 end'


def main():
	print u'''谷歌host修改脚本
author pop<hipop#126.com>
01/05/2015 -> 06/30/2016 modifyed by DDGG.
数据：http://www.360kb.com/kb/2_122.html
'''

	# load host from 360kb
	html = urllib2.urlopen(URL).read()
	m = re.search(PATT_CONTENT, html, re.S)
	year = m.group(1)
	hosts_content = m.group()
	hosts_content = hosts_content.replace('&nbsp;', ' ')
	hosts_content = hosts_content.replace('<span>', '')
	hosts_content = hosts_content.replace('</span>', '')
	hosts_content = hosts_content.replace('<br />', '')

	# write host file
	try:
		f = open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'r+')  #
	except IOError as e:
		if e.errno == 13:  # IOError: [Errno 13] Permission denied: 'C:\\Windows\\System32\\drivers\\etc\\hosts'
			print u'请以管理员权限运行！'
			os.system('pause')
			sys.exit(1)

	hosts_origin = f.read()
	reg = re.compile(r'\n#google=.*#google hosts %s end' % year, re.S)
	hosts_new = re.sub(reg, '', hosts_origin)
	hosts_new = hosts_new + '\n#google===========================\n' + hosts_content
	# 安全起见，不修改account相关（By DDGG：但不修改就无法正常访问gmail.com）
	# reg = re.compile(r'account', re.S)
	# hosts_new = re.sub(reg, 'OOXXaccount', hosts_new)
	print hosts_new
	f.truncate(0)
	f.seek(0)
	f.write(hosts_new)
	f.close()
	print 'ok'


if __name__ == '__main__':
	main()
