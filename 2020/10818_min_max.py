N=int(input())
i=list(0 for x in range(0,N))
tmp=list(map(int,input().split()))
for x in range(0,N):
    i[x]=tmp[x]
    
print(min(i), max(i))