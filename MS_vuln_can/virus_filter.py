



f = open('result.txt','r')
f2 = open('virus1.txt','w')
count = 1
for i in f:
    if 'Found Vuln MS17-010!' in i:
        i = i.replace('+',str(count))
        f2.write(i)
        count += 1
        
f.close()
f2.close()

