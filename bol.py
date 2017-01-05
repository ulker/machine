# -*- coding: utf-8 -*-
import csv



csvfile = open('/home/furkan/Masaüstü/karismis.csv', 'r').readlines()
filename = 1
for i in range(len(csvfile)):
	if i % 4101 == 0:
		open(str(filename) + '.csv', 'w+').writelines(csvfile[i:i+4101])
		filename +=1
