T=int(input())
count=0
sum=list()
while(1):
    A,B=input().split(',')
    A=int(A);B=int(B)
    
    if A<0 or A>10 or B<0 or B>10:
        break
    
    sum.append(A+B)
    count+=1
    
    if count==T:
        break
    
for i in sum:
    print(i)