#!/usr/bin/python3.6
import os
import sys
g = open("ny.txt","w")
f = open("256ch.txt",'r')
while True:
 line = f.readline().replace('\n','')
 path = #path
 if not line: break
 if int(len(os.listdir(path))) != 171:
  g.write(line+str(len(os.listdir(path)))+"\n")
f.close
g.write("\n")

f = open("2048ch.txt",'r')
while True:
 line = f.readline().replace('\n','')
 path = 
 if not line: break
 if int(len(os.listdir(path))) != 171:
  g.write(line+str(len(os.listdir(path)))+"\n")
f.close
g.write("\n")
f = open("4096ch.txt",'r')
while True:
 line = f.readline().replace('\n','')
 path = 
 if not line: break
 if int(len(os.listdir(path))) != 171:
  g.write(line+str(len(os.listdir(path)))+"\n")
f.close
g.write("\n")
f = open("16384ch.txt",'r')
while True:
 line = f.readline().replace('\n','')
 path = 
 if not line: break
 if int(len(os.listdir(path))) != 171:
  g.write(line+str(len(os.listdir(path)))+"\n")
f.close
g.close
