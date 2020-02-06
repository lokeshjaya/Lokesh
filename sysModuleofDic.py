import sys
n=int(input())
d=dict()
if(n>=3 and n<=100000):
    for i in range(0,n):
        name,number=input().split()
        d[name]=number
lines=sys.stdin.readlines()
for i in lines:
    n1=i.strip()
    if n1 in d:
        print("{}={}".format(n1,d[n1]))
    else:
        print("Not found")
