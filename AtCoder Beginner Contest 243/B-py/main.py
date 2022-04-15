N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
x = 0
for i in range(N):
  if A[i]==B[i]:
    x+=1
print(x)
print(2*N - len(set(A+B))- x)
