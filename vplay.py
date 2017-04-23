#!/usr/bin/python



#///////////bANNER
"""
          __        _______ _     ____ ___  __  __ _____ 
          \ \      / / ____| |   / ___/ _ \|  \/  | ____|
           \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|  
            \ V  V / | |___| |__| |__| |_| | |  | | |___  _   _   _ 
             \_/\_/  |_____|_____\____\___/|_|  |_|_____|(_| |_| |_)
                                               
                        Script Crearor: 
     _   _    _____ _    ____    _____  ___     ___    _   _    _    
    | | / \  |  ___/ \  |  _ \  |_   _|/ \ \   / / \  | \ | |  / \   
 _  | |/ _ \ | |_ / _ \ | |_) |   | | / _ \ \ / / _ \ |  \| | / _ \  
| |_| / ___ \|  _/ ___ \|  _ <    | |/ ___ \ V / ___ \| |\  |/ ___ \ 
 \___/_/   \_\_|/_/   \_\_| \_\   |_/_/   \_\_/_/   \_\_| \_/_/   \_\
                                                                     
Tell:  +989170118221   		  Mail: PowerInfoSSL@Gmail.com
"""
##




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
