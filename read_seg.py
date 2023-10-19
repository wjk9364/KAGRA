#!usr/bin/python3.6

import os
import sys
import subprocess
import re
import tailer
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("-y", "--year", action="store", type=int)
parser.add_argument("-m", "--month", action="store", type=int)
parser.add_argument("-d", "--day", action="store", type=int)
args = parser.parse_args()

year = args.year
month = args.month
day = args.day

if month >= 10:
        if day >= 10:
                date=str("{0}-{1}-{2}".format(year,month,day))
        else:
                date=str("{0}-{1}-0{2}".format(year,month,day))
else:
        if day >= 10:
                date=str("{0}-0{1}-{2}".format(year,month,day))
        else:
                date=str("{0}-0{1}-0{2}".format(year,month,day))
gps_s = int(os.popen("tconvert {0}".format(date)).read())
gps_e = gps_s + 86400
f = open("/data/kagra/home/chihiro.kozakai/K1Segments/DET_FOR_GRB200415A/K1-DET_FOR_GRB200415A_UTC_{0}.txt".format(date),'r')
lines = f.readlines()
tail = str(tailer.tail(open("/data/kagra/home/chihiro.kozakai/K1Segments/DET_FOR_GRB200415A/K1-DET_FOR_GRB200415A_UTC_{0}.txt".format(date)),1))
tail = tail.strip("[]'")

total = 0
g = open("segments.txt",'w')
for line in lines:
	line = line.strip('\n')
	start = int(re.findall('\d+',line)[0])
	end = int(re.findall('\d+',line)[1]) - 30
	if end == gps_e:
		end = end + 2
	else :
		end = end
	if start > end:
		continue
	if start == end:
		continue
	g.write("{0} {1}\n".format(start,end))
	total = end-start + total
	if line == tail:
		avg = total/4
f.close()
g.close()

f = open("/data/kagra/home/chihiro.kozakai/K1Segments/DET_FOR_GRB200415A/K1-DET_FOR_GRB200415A_UTC_{0}.txt".format(date),'r')

lines = f.readlines()
total = 0
i = 1
n_seg = 4

for j in range(1,n_seg+1):
	g = open("segments_{0}.txt".format(j),'w')
	g.close()
for line in lines:
	start = int(re.findall('\d+',line)[0])
	end = int(re.findall('\d+',line)[1])
	if end == gps_e:
		end = end + 2
	else :
		end = end - 30
	if start > end:
		tmp = start
		start = end
		end = tmp
	if start == end:
		continue
	total = end - start + total
	g = open("segments_{0}.txt".format(i),'a')
	g.write("{0} {1}\n".format(start,end))
	if total > avg * i:
		i = i + 1
	if i > 4:
		i = 4
	g.close()
f.close()


