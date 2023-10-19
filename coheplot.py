#!/usr/bin/env python
import numpy
import sys
import matplotlib
import subprocess
import os
import argparse

from gwpy.timeseries import TimeSeries
from gwpy.time import tconvert
from glue.lal import Cache
from gwpy.segments import Segment
from termcolor import colored
from multiprocessing import Process, Queue

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("-y", "--year", action="store", type=int)
parser.add_argument("-m", "--month", action="store", type=int)
parser.add_argument("-d", "--day", action="store", type=int)
parser.add_argument("-t","--time",action="store",type=float)
parser.add_argument("-dur","--duration",action="store",type=float)
args = parser.parse_args()

year = args.year
month = args.month
day = args.day
dur = args.duration
time = args.time

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

matplotlib.use('Agg')
if not os.path.exists('./{0}'.format(date)):
 subprocess.call('mkdir {0}'.format(date),shell=True)
# Read main cache
gwf_cache = '/data/kagra/home/kihyun.jung/Omicron/1daymkOmicron/{0}-gwf.lcf'.format(date)

with open(gwf_cache, 'r') as fobj:
 cache = Cache.fromfile(fobj)

### Read Timeseries Data ###
 gst = time - dur/2
 get = time + dur/2
 com_ch1 = 'K1:PEM-ACC_EXC_CHAMBER_EXC_Z_OUT_DQ'
 ch1 = TimeSeries.read(cache, com_ch1, start=gst, end=get, format='gwf.lalframe')

 f=open('chlist.txt','r')
 line_num = 1
 com_ch2 = f.readline()
 com_ch2 = com_ch2.strip('\n')
 while com_ch2:
  try:
   ch2 = TimeSeries.read(cache, com_ch2, start=gst, end=get, format='gwf.lalframe')
   ch2_name = com_ch2.strip('K1:')

########### Coherence plot ###########
   coh = ch1.coherence(ch2, fftlength=2, overlap=1)
   coh_plot = coh.plot(figsize=[12, 6])
   ax = coh_plot.gca()
   ax.set_xlabel('Frequency [Hz]')
   ax.set_ylabel('Coherence')
   ax.set_yscale('linear')
   maxx = float(str(coh.xindex[-1]).split(' ')[0])
   ax.set_xlim(1,maxx)
   ax.set_ylim(0, 1)
   ax.set_title('Coherence between two channels')
   coh_plot.savefig('{0}/CHAMBER&{1}_Coherence_{2}.png'.format(date,ch2_name,time))
   com_ch2 = f.readline()
   com_ch2 = com_ch2.strip('\n')
  except:
   com_ch2 = f.readline()
   com_ch2 = com_ch2.strip('\n')
   continue
 f.close()

