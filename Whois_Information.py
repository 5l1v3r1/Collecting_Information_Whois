#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket, sys
import os
import time
P  = '\033[35m'
GR = '\033[37m' # gray
os.system('clear')
black_Barry= """
          █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
          █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
          █░░║║║╠─║─║─║║║║║╠─░░█ 
          █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█       Collecting Information
          █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ 
          ▒▒▄▀▀▀▀▀▄▒▒▒▒▒▄▄▄▄▄▒▒▒
          ▒▐░▄░░░▄░▌▒▒▄█▄█▄█▄█▄▒
          ▒▐░▀▀░▀▀░▌▒▒▒▒▒░░░▒▒▒▒
          ▒▒▀▄░═░▄▀▒▒▒▒▒▒░░░▒▒▒▒
          ▒▒▐░▀▄▀░▌▒▒▒▒▒▒░░░▒▒▒▒
        +=========================+
        |   łαbørαŧøriø Fαηŧαsмα  |
        +=========================+
        | Coded : łuŧЋ1єr         |
        | Channel: @Phantasm_Lab  |
        | Date : 18:05:2017       |
        | https://goo.gl/f4EPw1   |
        +=========================+
        +=========================+
"""
print('')
print(GR+black_Barry)
def Animation(String):
    animation = "|/-\\"
    for i in range(15):
        time.sleep(0.1)
        sys.stdout.write("\r" + "[" + animation[i % len(animation)] + "]" + P + String)
        sys.stdout.flush()
    print('\n')

def black_whois(server , query) :
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.connect((server , 43))
    s.send(query + '\r\n')
    msg = ''
    while len(msg) < 10000:
        chunk = s.recv(100)
        if(chunk == ''):
            break
        msg = msg + chunk
     
    return msg
def get_whois(domain):
    domain = domain.replace('http://','')
    domain = domain.replace('www.','')
    ext = domain[-3:]
    if(ext == 'com' or ext == 'org' or ext == 'net'):
        whois = 'whois.internic.net'
        msg = black_whois(whois , domain)
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if  'Whois' in words[0] and 'whois.' in words[1]:
                    whois = words[1].strip()
                    break;
    else:
        ext = domain.split('.')[-1]
        whois = 'whois.iana.org'
        msg = black_whois(whois , ext)
        lines = msg.splitlines()
        for line in lines:
            if ':' in line:
                words = line.split(':')
                if 'whois.' in words[1] and 'Whois Server (port 43)' in words[0]:
                    whois = words[1].strip()
                    break;
    msg = black_whois(whois , domain)
    return msg
try:
	domain_name = sys.argv[1]
except:
	print('\n Usage > python2 Whois_Information.py <url>')
	print('\n Usage > python2 Whois_Information.py pf.gov.br\n') 
	exit()
print('')
Animation(' Collecting Information, Please Wait....')
print get_whois(domain_name)
