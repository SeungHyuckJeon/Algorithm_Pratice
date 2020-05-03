num=list()
for i in range(0,9):
    num.append(int(input()))

print(max(num), num.index(max(num))+1)