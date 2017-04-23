#!/usr/bin/python
from time import sleep
import sys,os
from glob import glob
#print len(sys.argv)
#if len(sys.argv) !=2:
#    print '\n\n Correct Form is ScripName Extention.'
#    sys.exit()
os.system('clear')
#ex=sys.argv[1]
f=glob('*.mp4')
print '\n%s Selected.\n' % len(f)
for i in f:
    print '\n [+] Playing %s \n' % i
    os.system("omxplayer '%s'" % i)
    sleep(2)
