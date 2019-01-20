import os
import sys
import datetime
import time

host=sys.argv[1]

if host =="-h" or host =="-help":
    print("Usage: test.py [host] \n")

tping = True if os.system("ping "+host+" -c 1") is 0 else False

if tping == False:
    print("Unable to reach host: host is invalid!!")
    exit()

current = datetime.datetime.now()
file = "/home/alex/Desktop/new_scan_"+str(current)

ofile = open(file , 'w')
hping = os.popen('hping3 --scan 1-65535 -S '+host).read()
ofile.write(hping)
if "80" in hping:
    nik = os.popen('nikto -host '+host).read()
    ofile.write(nik)
time.sleep(10)
if "8080" in hping:
    nik = os.popen("nikto -host "+host+" -port 8080").read()
    ofile.write(nik)
time.sleep(10)
if "21" in hping:
    ftp = os.popen("/opt/ftp-user-enum/ftp-user-enum\.pl -M iu -U /home/alex/usernames\.txt  -t "+str(host)).read()
    ofile.write(ftp)
time.sleep(10)
if "139" in hping or "445" in hping:
    enum = os.popen('/opt/enumlin/enum4linux/enum4linux\.pl '+str(host)).read()
    ofile.write(enum)
time.sleep(10)
nserv = os.popen('nmap -sV -sC -v -T5 '+host).read()
ofile.write(nserv)
ofile.close()