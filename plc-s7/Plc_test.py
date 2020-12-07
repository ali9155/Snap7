import S71200
from time import sleep


myplc = S71200.S71200('192.168.1.151')

while(True):
    
    myplc.writeMem('qx0.0',True)
    #sleep(1)    
    myplc.writeMem('qx0.0',False)
    #sleep(1)
   
