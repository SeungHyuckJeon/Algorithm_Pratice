N = input()

a=list(N)
a.sort(reverse=True)

result=""
for i in a:
    result+=i
    
print(result)