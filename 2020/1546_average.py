N = int(input())
scores = list(map(int,input().split()))

if len(scores)>N or len(scores)<N:
	exit()

max = 0
for i in scores:
	if max<i:
		max=i

newscore = list()
sum=0
for i in range(0,N):
	newscore.append(scores[i]/max*100)
	sum += newscore[i]

newavg = sum/N
print(newavg)