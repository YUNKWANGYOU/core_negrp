import sys
reload(sys) 
sys.setdefaultencoding('utf-8')
import socket
from datetime import datetime
import os 

os.chdir('/home/ssnoc/core_negrp/tracertData')
preFix = "tracert"
sufFix = ".log"

bindIP = "60.30.39.123"
bindPORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((bindIP,bindPORT))

while True :
    data, addr = sock.recvfrom(9000000)
    print (data.decode(), addr)
    curDay = datetime.now().strftime('%Y%m%d')
    logFile = (preFix+curDay+sufFix)
    with open (logFile,'a') as f :
        f.write(data.decode())