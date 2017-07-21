#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket,time

file_object = open('ip.txt')
for line in file_object:
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ip = line.split()[0]
        port = int(line.split()[1])
        print(ip,port)
        sk.settimeout(1)
        sk.connect((ip,port))
        timenow = time.localtime()
        datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
        logstr = "%s:%s 连接成功->%s \n" % (ip, port, datenow)
        print(logstr)
        sk.close()
    except Exception:
        file = open("ip_port.log","a")
        timenow = time.localtime()
        datenow = time.strftime('%Y-%m-%d %H:%M:%S', timenow)
        logstr = "%s:%s 连接不成功->%s \n" % (ip, port, datenow)
        print(logstr)
        sk.close()
        file.close()
