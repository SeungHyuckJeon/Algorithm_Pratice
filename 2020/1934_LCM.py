T=int(input())
count=0
result=list()
def gcd(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

def lcm(a,b):
    return int(a*b/gcd(a,b))

while(1):
    a,b=map(int,input().split())
    result.append(lcm(a,b))
    count+=1
    if count==T:
        for i in result:
            print(i)
        break