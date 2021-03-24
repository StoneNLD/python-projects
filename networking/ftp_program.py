#!/usr/bin/env python

from ftplib import FTP

#domain name or server ip:
ftp = FTP('0.0.0.0')
ftp.login(user='user', passwd = '12345')

def placeFile():
    filename = 'exampleFile.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

def grabFile():
    filename = 'kaasfiets'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

#placeFile()
grabFile()
