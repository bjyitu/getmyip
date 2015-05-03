#!/usr/bin/env python
# coding=utf-8

import re

import urllib2
import os


class Getmyip:

    def getip(self):
        try:
            myip = self.visit("http://www.123cha.com")
            #myip = self.visit("http://1111.ip138.com/ic.asp")
            #myip = self.visit("http://ip.chinaz.com")
            #myip = self.visit("http://ip.lockview.cn")
            #myip = self.visit("http://ip.cn")
            return myip
        except:
            #myip = self.visit("http://www.123cha.com")
            myip = self.visit("http://www.133ip.com")
            return myip

    def visit(self, url):
        opener = urllib2.urlopen(url, data=None, timeout=5)
        if url == opener.geturl():
            str = opener.read()
            strip = re.compile(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', re.IGNORECASE)
            return re.search(strip, str).group(0)

getmyip = Getmyip()
localip = getmyip.getip()
#print localip
os.system("echo '%s' | mail -s HomeIp sgwangchao@163.com" % localip)
