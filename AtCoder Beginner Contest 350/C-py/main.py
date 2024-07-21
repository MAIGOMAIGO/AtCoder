N = int(input())
A = list(map(int,input().split()))
D = {A[i]:i+1 for i in range(N)}
a = []
for i in range(1,N+1):
  if D[i] != i:
    a.append([i,D[i]])
    t = D[i]
    D[i] = i
    D[A[i-1]] = t
    A[t-1] = A[i-1]
    A[i-1] = i
print(len(a))
for i in a:
  print(*i)