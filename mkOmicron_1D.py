# /usr/bin/python3.6

import os
import subprocess
import sys
import argparse

# Read Time information #
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

print("Start Generate Omicron at {0}.".format(date))

gpsstart = int(os.popen("tconvert {0}".format(date)).read())
gpsend = gpsstart + 86400

print("GPS time : {0} ~ {1}".format(gpsstart, gpsend))

# Make Cache #
gwf_path1 = int(gpsstart/100000)
gwf_path2 = int(gpsend/100000)

# ffl cache
if gwf_path1 == gwf_path2:
	subprocess.call("python3.6 mkcache_path2ffl.py -s {0} -e {1} -o {2}-gwf.ffl -p '{3}/*.gwf'".format(gpsstart,gpsend,date,gwf_path1),shell=True)
	subprocess.call("python3.6 mkcache_path2ffl.py -s {0} -e {1} -o {2}-DAC-gwf.ffl -p '{3}/*.gwf'".format(gpsstart,gpsend,date,gwf_path1),shell=True)
else:
	subprocess.call("python3.6 mkcache_path2ffl.py -s {0} -e {1} -o {2}-gwf.ffl -p '{3}/*.gwf','{4}/*.gwf'".format(gpsstart,gpsend,date,gwf_path1,gwf_path2),shell=True)
	subprocess.call("python3.6 mkcache_path2ffl.py -s {0} -e {1} -o {2}-DAC-gwf.ffl -p '{3}/*.gwf','{4}/*.gwf'".format(gpsstart,gpsend,date,gwf_path1,gwf_path2),shell=True)

# Replacing PATH of parameter file
subprocess.call("python3.6 repl_path.py {0} {1} {2}".format(year,month,day),shell=True)

# Generate Omicron #
dir_name = date
dir_path = # Output dieretory path
if not os.path.exists(dir_path):
	os.mkdir(dir_path)

'''
gps1 = gpsstart + 21600
gps2 = gps1 + 21600
gps3 = gps2 + 21600
f = open("segments.txt",'w')
f.write("{0} {1}".format(gpsstart, gpsend))
f.close()
f = open("segments_1.txt",'w')
f.write("{0} {1}".format(gpsstart, gps1))
f.close()
f = open("segments_2.txt",'w')
f.write("{0} {1}".format(gps1, gps2))
f.close()                                                                        
f = open("segments_3.txt",'w')
f.write("{0} {1}".format(gps2, gps3))
f.close()                                                                                           
f = open("segments_4.txt",'w')
f.write("{0} {1}".format(gps3, gpsend))
f.close()
subprocess.call("chmod 755 segments*",shell=True)
'''
subprocess.call("python3.6 read_seg.py -y {0} -m {1} -d {2}".format(year,month,day),shell=True)

# Condor Submit
# 2048Hz Divided as 6, 16384Hz Divided as 8 
# Time segments are divided as 4 (21600 sec = 6 hour)
# 1024 : 1 * 4 | 2048 : 6 * 4 | 16384 : 8 * 4

if not os.path.exists('./logs'):
	os.mkdir('logs')

subprocess.call("condor_submit omicron-256.sub",shell=True)
subprocess.call("condor_submit omicron-512.sub",shell=True)
subprocess.call("condor_submit omicron-4096.sub",shell=True)
subprocess.call("condor_submit omicron-DAC.sub",shell=True)
n_seg = 4
dv_1024 = 1
dv_2048 = 6
dv_16384 = 8

for i in range(1,dv_1024+1):
	for j in range(1,n_seg+1):
		subprocess.call("python3.6 mksub.py 1024 {0} {1}".format(i,j),shell=True)
		subprocess.call("chmod 755 omicron-1024-{0}-{1}.sub".format(i,j),shell=True)
		subprocess.call("condor_submit omicron-1024-{0}-{1}.sub".format(i,j),shell=True)
for i in range(1,dv_2048+1):
	for j in range(1,n_seg+1):
		subprocess.call("python3.6 mksub.py 2048 {0} {1}".format(i,j),shell=True)
		subprocess.call("chmod 755 omicron-2048-{0}-{1}.sub".format(i,j),shell=True)
		subprocess.call("condor_submit omicron-2048-{0}-{1}.sub".format(i,j),shell=True)
#for i in range(1,dv_16384+1):
#	for j in range(1,n_seg+1):
#		subprocess.call("python3.6 mksub.py 16384 {0} {1}".format(i,j),shell=True)
#		subprocess.call("chmod 755 omicron-16384-{0}-{1}.sub".format(i,j),shell=True)
#		subprocess.call("condor_submit omicron-16384-{0}-{1}.sub".format(i,j),shell=True)

print("Generating Omicron at {0}.".format(date)) 
print("Please check condor job using 'condor_q'.")














