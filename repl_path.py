#usr/bin/python3.6

import fileinput
import sys

year = int(float(sys.argv[1]))
month = int(float(sys.argv[2]))
day = int(float(sys.argv[3]))

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

path_FFL = # Cache path
path_output = # Output path
dv_1024 = 1
dv_2048 = 6
dv_16384 = 8
print("Replacing file path of parameters-kagra...")

for line in fileinput.input('./parameters-kagra-DAC.txt', inplace = True):
        if 'DATA FFL' in line:
                line = line.replace(line, 'DATA FFL {0}{1}-DAC-gwf.ffl\n'.format(path_FFL,date))
        if 'OUTPUT DIRECTORY' in line:
                line = line.replace(line, 'OUTPUT DIRECTORY {0}{1}\n'.format(path_output,date))
        sys.stdout.write(line)

for line in fileinput.input('./parameters-kagra-256.txt', inplace = True):
	if 'DATA FFL' in line:
		line = line.replace(line, 'DATA FFL {0}{1}-gwf.ffl\n'.format(path_FFL,date))
	if 'OUTPUT DIRECTORY' in line:
		line = line.replace(line, 'OUTPUT DIRECTORY {0}{1}\n'.format(path_output,date))
	sys.stdout.write(line)

for line in fileinput.input('./parameters-kagra-512.txt', inplace = True):
	if 'DATA FFL' in line:
		line = line.replace(line, 'DATA FFL {0}{1}-gwf.ffl\n'.format(path_FFL,date))
	if 'OUTPUT DIRECTORY' in line:
		line = line.replace(line, 'OUTPUT DIRECTORY {0}{1}\n'.format(path_output,date))
	sys.stdout.write(line)

for i in range (1, dv_1024+1):
	for line in fileinput.input('./parameters-kagra-1024-{0}.txt'.format(i), inplace = True):
		if 'DATA FFL' in line:
			line = line.replace(line, 'DATA FFL {0}{1}-gwf.ffl\n'.format(path_FFL,date))
		if 'OUTPUT DIRECTORY' in line:
			line = line.replace(line, 'OUTPUT DIRECTORY {0}{1}\n'.format(path_output,date))
		sys.stdout.write(line)
for i in range (1, dv_2048+1):
	for line in fileinput.input('./parameters-kagra-2048-{0}.txt'.format(i), inplace = True):
		if 'DATA FFL' in line:
			line = line.replace(line, 'DATA FFL {0}{1}-gwf.ffl\n'.format(path_FFL,date))   
		if 'OUTPUT DIRECTORY' in line:
			line = line.replace(line, 'OUTPUT DIRECTORY {0}{1}\n'.format(path_output,date))
		sys.stdout.write(line)
for line in fileinput.input('./parameters-kagra-4096.txt', inplace = True):
 	if 'DATA FFL' in line:
  		line = line.replace(line, 'DATA FFL {0}{1}-gwf.ffl\n'.format(path_FFL,date))   
 	if 'OUTPUT DIRECTORY' in line:
  		line = line.replace(line, 'OUTPUT DIRECTORY {0}{1}\n'.format(path_output,date))
 	sys.stdout.write(line)
"""
for i in range (1, dv_16384+1):
	for line in fileinput.input('./parameters-kagra-16384-{0}.txt'.format(i), inplace = True):
 		if 'DATA FFL' in line:
  			line = line.replace(line, 'DATA FFL {0}{1}-gwf.ffl\n'.format(path_FFL,date))  
 		if 'OUTPUT DIRECTORY' in line:
  			line = line.replace(line, 'OUTPUT DIRECTORY {0}{1}\n'.format(path_output,date))
 		sys.stdout.write(line)
"""
print("Done")










