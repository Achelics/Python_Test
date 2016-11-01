#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'achelics'
__Date__ = '2016/9/25'

import urllib2
import urllib
import requests
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth

data = dict()
data['userId'] = '2015E8018661105'
data['password'] = '123456'
data['service'] = ''
data['queryString'] = 'wlanuserip%3D0bc386d9e643d188b011a0d00c9b5c40%26wlanacname%3D5fcbc245a7ffdfa4%26ssid%3D%26nasip%3D2c0716b583c8ac3cbd7567a84cfde5a8%26mac%3D53ba540bde596b811a6d5617a86fa028%26t%3Dwireless-v2%26url%3D2c0328164651e2b4f13b93'
data['operatorPwd'] = ''
data['validcode'] = ''

# 定义post的地址
url = 'http://210.77.16.21/eportal/InterFace.do?method=login'
post_data = urllib.urlencode(data)

# 提交，发送数据
req = urllib2.urlopen(url, post_data, timeout=3)
# 获取提交后返回信息
content = req.read()
print content
