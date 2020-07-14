N = int(input())
word=[]
word_sorted=[]

for i in range(0,N):
    tmp=input()
    word.append(tmp)

#소문자인지 판별
for i in word:
    if i.islower() and i not in word_sorted:
        word_sorted.append(i)
        
#짧은거부터 정렬
word_sorted.sort()
word_sorted.sort(key=len)

for i in word_sorted:
    print(i)