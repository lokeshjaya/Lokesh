a=int(input())
l1=[]
for i in range(a+1):
  x=1
  l2=[]
  for j in range(i+1):
    l2.append(x)
    X=X*(i-j)//(j+1)
  l1.append(l2)
print(*l1[a])
  
