#!/usr/bin/env python
import os
pwd = os.getcwd()
cs_db_name = 'cscope.out'
init = 1
while pwd !="":
    t = 0
    if init != 1:
        t = pwd.rfind('/')
    else:
        t = len(pwd)
        init = 0

    print pwd
    if t !=-1:
        cs_db = pwd[0:t] + '/' + cs_db_name
        print cs_db
        if os.access(cs_db,os.R_OK) == True:
            print "CSCOPE_DB=" + cs_db
            cmd = "cd " + pwd[0:t] + ";CSCOPE_DB=" + cs_db + " vim"          
            os.system(cmd)
            break
        else:
            pwd = pwd[0:t]
    else:
        print "ohoooo"
        break
