#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Ahelcis'
__Date__ = '2016/10/08'

import re

pattern = r'/(\d)(?=((\d{3}+)$)/'
data = '12334565632'

print re.match(pattern, data)
