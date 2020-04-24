import sys
import time
start=time.time()
count=0
N=int(input())
if N>99 or N<0:
    sys.exit()
    
d=N
while True:
    count+=1
    a=d//10; b=d%10
    c=a+b
    d=b*10+c%10
    if d==N:
        break
    
print('result: ',count)
print('time:',time.time()-start)