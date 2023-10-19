#/usr/bin/python3.6

import sys
import os
Hz = int(float(sys.argv[1]))
dv_ch = int(float(sys.argv[2]))
n_seg = int(float(sys.argv[3]))

f = open('omicron-{0}-{1}-{2}.sub'.format(Hz, dv_ch, n_seg),'w')
f.write('universe = vanilla\n')
f.write('executable = /cvmfs/oasis.opensciencegrid.org/ligo/sw/conda/envs/igwn-py36/bin/omicron\n')
f.write('arguments = ./segments_{0}.txt ./parameters-kagra-{1}-{2}.txt\n'.format(n_seg, Hz, dv_ch))
f.write('environment = KMP_LIBRARY=serial;MKL_SERIAL=yes\n')
f.write('request_cpus = 1\n')
f.write('request_memory = 4*2048\n')
f.write('getenv = True\n')
f.write('log = logs/omicron-{0}-{1}-{2}.log\n'.format(Hz, dv_ch, n_seg))
f.write('error = logs/omicron-{0}-{1}-{2}.err\n'.format(Hz, dv_ch, n_seg))
f.write('output = logs/omicron-{0}-{1}-{2}.out\n'.format(Hz, dv_ch, n_seg))
f.write('notification = never\n')
f.write('requirements = (Machine != "ldg-wn2006.sdfarm.kr") && (Machine != "ldg-wn2008.sdfarm.kr") && (Machine != "ldg-wn2016.sdfarm.kr") && (Machine != "ldg-wn2018.sdfarm.kr") && (Machine != "ldg-wn2026.sdfarm.kr") && (Machine != "ldg-wn2047.sdfarm.kr") && (Machine != "ldg-gpu03.sdfarm.kr") && (Machine != "ldg-wn2031.sdfarm.kr") && (Machine != "ldg-wn2049.sdfarm.kr") && (Machine != "ldg-wn2033.sdfarm.kr") && (Machine != "ldg-wn2010.sdfarm.kr") && (Machine != "ldg-wn2037.sdfarm.kr") && (Machine != "ldg-wn2020.sdfarm.kr") && (Machine != "ldg-wn2022.sdfarm.kr") && (Machine != "ldg-wn2002.sdfarm.kr") && (Machine != "ldg-wn2012.sdfarm.kr") && (Machine != "ldg-wn2032.sdfarm.kr") && (Machine != "ldg-wn2014.sdfarm.kr") && (Machine != "ldg-wn2024.sdfarm.kr") && (Machine != "ldg-wn2004.sdfarm.kr") && (Machine != "ldg-wn2060.sdfarm.kr") && (Machine != "ldg-wn2043.sdfarm.kr") && (Machine != "ldg-wn2045.sdfarm.kr") && (Machine != "ldg-wn2048.sdfarm.kr") && (Machine != "ldg-wn2058.sdfarm.kr")\n')
f.write('queue 1\n')
f.close()

