

import os,re


hostlist = []

def taskruner():
        
    f = open('hosts-ip.txt','r')
    f2 = open('checkhost.txt','a+')
    for i in f:
        print (i)
        result = re.findall(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b",str(i))
        
        f2.write(str(result)+'\n')

    f.close()
    f2.close()


if __name__== '__main__':
    print ('it begain to start check ....')
    taskruner()

             
             
        
