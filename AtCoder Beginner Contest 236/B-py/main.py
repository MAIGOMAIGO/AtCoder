N = int(input())
A = list(map(int,input().split()))
A.sort()
a = N
for i in range(N-1):
  if A[4*i] != A[4*i+3]:
    a = A[4*i]
    break
print(a)
