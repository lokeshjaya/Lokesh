from collections import Counter
n=int(input())
for i in range(n):
  l=[]
  m=int(input())
  l1=list(map(int,input().split()))
  temp=Counter(l1)
  for i,j in temp.items():
    l.append(j)
  print(l.count(2))
