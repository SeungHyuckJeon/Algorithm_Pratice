N = int(input())
if N<3 or N>5000:
  exit()

i=-1
result=9999

while(1):
  i+=1
  newresult=0

  tmp=N-(5*i)
  if tmp<0:
    if result==9999:
      result=-1
    break

  if tmp%3==0:
    newresult+=int(tmp/3)
    newresult+=i
    if result>newresult:
      result=newresult
  
print(result)