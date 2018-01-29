#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 2017/12/21

import os



def taskruner1():
    for i in range(1,250):
        result = os.system(r"MS_17_010_Scan.exe -ip 10.103.%d.1 10.103.%d.254" %(i,i))
    print ('10.103.0.0/16 test finished.')

def taskruner2():
    for i in range(1,250):
        result = os.system(r"MS_17_010_Scan.exe -ip 10.6.%d.1 10.6.%d.254" %(i,i))
    print ('10.6.0.0/16 test finished.')
    
        
def taskruner3():
    for i in range(1,250):
        result = os.system(r"MS_17_010_Scan.exe -ip 10.7.%d.1 10.7.%d.254" %(i,i))
    print ('10.7.0.0/16 test finished.')



def taskruner4():
    for i in range(1,250):
        result = os.system(r"MS_17_010_Scan.exe -ip 10.8.%d.1 10.8.%d.254" %(i,i))
    print ('10.8.0.0/16 test finished.')


def taskruner5():
    for i in range(1,250):
        result = os.system(r"MS_17_010_Scan.exe -ip 10.190.%d.1 10.190.%d.254" %(i,i))
    print ('10.190.200.0/24 test finished.')

def taskruner6():
    for i in range(1,20): 
        result = os.system(r"MS_17_010_Scan.exe -ip 10.188.%d.1 10.188.%d.254" %(i,i))
    print ('10.188.0.0/16 test finished.')




if __name__== '__main__':
    print ('it begain to start the "Scan.exe" ....')
    taskruner1()
    taskruner2()
    taskruner3()
    taskruner4()
    taskruner5()
    taskruner6()
    

    print ('it finished to scan all subnet.')





#    task = [taskruner1()，taskruner2()，taskruner3()，taskruner4()，taskruner5()，taskruner6()]
#    for i in task:
#        i
    
    









    
