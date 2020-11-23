import sys

def mergesort(list):
    if len(list)<=1:
        return list

    mid = len(list)//2
    leftlist = list[:mid]
    rightlist = list[mid:]
    mergesort(leftlist)
    mergesort(rightlist)

    left = 0
    right = 0
    current = 0
    while left<len(leftlist) and right < len(rightlist):
        if leftlist[left] < rightlist[right]:
            list[current] = leftlist[left]
            left+=1
            current+=1
        else:
            list[current] = rightlist[right]
            right+=1
            current+=1
    while left<len(leftlist):
        list[current] = leftlist[left]
        left+=1
        current+=1
    while right<len(rightlist):
        list[current] = rightlist[right]
        right+=1
        current+=1
    

N = int(sys.stdin.readline())

list=[int(sys.stdin.readline()) for i in range(N)]

mergesort(list)
for i in list:
  print(i)