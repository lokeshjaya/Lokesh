n=int(input())
s=input().split()
val=int(input())
for i in range(val):
  s=s[-1:]+s[:-1]
for i in s:
  print(i,end="")
