import os

f = open('checkhost.txt','r')



def taskruner6():
    for i in f:
        #print (type(i))
        w = i[2:-4]
        #for n in i:
        #    print (n)
        result = os.system(r"MS_17_010_Scan.exe -ip %s" %(w))
    print ('%s test finished.' %(w))




if __name__== '__main__':
    print ('it begain to start the "Scan.exe" ....')
    taskruner6()
