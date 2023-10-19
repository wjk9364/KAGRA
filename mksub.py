#/usr/bin/python3.6

import sys
import os
Hz = int(float(sys.argv[1]))
dv_ch = int(float(sys.argv[2]))
n_seg = int(float(sys.argv[3]))

f = open('omicron-{0}-{1}-{2}.sub'.format(Hz, dv_ch, n_seg),'w')
f.write('universe = vanilla\n')
f.write('executable = [Executable omicron file path]\n')
f.write('arguments = ./segments_{0}.txt ./parameters-kagra-{1}-{2}.txt\n'.format(n_seg, Hz, dv_ch))
f.write('environment = KMP_LIBRARY=serial;MKL_SERIAL=yes\n')
f.write('request_cpus = 1\n')
f.write('request_memory = 4*2048\n')
f.write('getenv = True\n')
f.write('log = logs/omicron-{0}-{1}-{2}.log\n'.format(Hz, dv_ch, n_seg))
f.write('error = logs/omicron-{0}-{1}-{2}.err\n'.format(Hz, dv_ch, n_seg))
f.write('output = logs/omicron-{0}-{1}-{2}.out\n'.format(Hz, dv_ch, n_seg))
f.write('notification = never\n')
f.write('queue 1\n')
f.close()

