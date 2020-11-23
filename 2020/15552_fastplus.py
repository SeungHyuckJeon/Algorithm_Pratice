import sys

N = int(sys.stdin.readline())
list=[]

for i in range(0,N):
    a, b = map(int,sys.stdin.readline().split())
    list.append(a+b)

for i in list:
    print(i)