#!/usr/bin/env python3 
'''
Enrique Molina 164024226
'''
import os
import sys
'''
This Script is to audit the Samba log files to see who is currently accessing the samba filesystem, on what operating system, what time, the IP address, which file accessed. 
'''

SambaLogFile = "/var/log/syslog" 

def LastLogsSB(): 
    #To get the last few logs with tail from the file
    logcmd = f"tail -30 {SambaLogFile}" 
    inp = os.popen(logcmd)
    outp = inp.read()
    print(outp)
    print ("last 30 Samba Log Files")

    for line in outp.splitlines(): 
        try: 
            prefix, audit = line.split("smbd_audit: ") 
            parts = audit.split("|")

            if len(parts) < 4:
                continue

            user = parts[0]
            ip = parts[1]
            action = parts[2]
            file_path = parts[3]


            print(f"Time: {prefix.strip()}")
            print(f"User: {user}")
            print(f"Ip: {ip}")
            print(f"Action: {action}")
            print(f"File: {file_path}")

        except Exception as e: 
            continue
                  





if __name__ == "__main__": 
    LastLogsSB() 

    
