n=int(input())
matrix=[]
l=[]
l1=[]

'''getting the matrix'''
for i in range(n):
     arr=[]
     for j in range(n):
          arr.append(int(input()))
     matrix.append(arr)
'''printing the matrix'''
for i in range(n):
     for j in range(n):
          print(matrix[i][j],end=' ')
     print()
'''printing diagonal'''
for i in range(n):
     for j in range(n):
          
          if([i]==[j]):
               b=matrix[i][j]
               l.append(b)
'''printing opposite diagonal'''        
for i in range(n):
     a=matrix[n-i-1][i]
     l1.append(a)
print(sum(l)-sum(l1))


