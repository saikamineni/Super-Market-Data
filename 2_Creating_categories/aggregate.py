#!/usr/bin/python

from __future__ import with_statement
import csv, re

@outputSchema("Category:chararray")

def create(input,path):
	
	with open(path, 'r') as f:
		rowdata = []
		reader  = csv.reader(f)
		reader.next()
		for row in reader:
			rowdata.append(row)
			
		for num1 in range(0, len(rowdata)):
			if (re.match(input, rowdata[num1][0])):
				flag = 1
				return (rowdata[num1][1])
			else:
				flag = 0
		if (flag == 0):
			return "UNCATEGORIZED" 
	
