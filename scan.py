import socket, subprocess, sys
from datetime import datetime

subprocess.call('clear',shell=True)
rmip = raw_input('Enter Remote Host to Scan: ')
r1 = int(raw_input('Enter the start Port Number '))
r2 = int(raw_input('Enter the last Port Number '))
print('*'*40)
print('Scanner Working on ', rmip)
print('*'*40)

t1 = datetime.now()
try:
    for port in range(r1,r2):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        result = sock.connect_ex((rmip, port))
        if result == 0:
            print("Port ->>> Open \t", port )
        sock.close()
except KeyboardInterrupt:
    print('Program interrupted by the User')
    sys.exit()
except socket.gaierror:
    print("Host name ", rmip ," Could not be resolved")
    sys.exit()
except socket.error:
    print("Could not connect to server ", rmip)
    sys.exit()
    
t2 = datetime.now()
total = t2 - t1
print('Time slapsed ', total)    
    