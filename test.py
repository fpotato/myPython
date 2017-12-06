#!/usr/bin/python
#-*- coding: UTF-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import bisect 

def grade(score, breakpoints=[60,70,80,90], grades = 'FDCBA'):
	i = bisect.bisect(breakpoints,score)
	return grade[i]

print(grade(10))