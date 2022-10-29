N = int(input())
A = list(map(int,input().split()))
L = []
for i in range(N-1):
  for j in range(i+1,N):
    L.append(abs(A[i]-A[j]))
print(max(L))
