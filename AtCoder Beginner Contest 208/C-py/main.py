N,K = map(int,input().split())
a = list(map(int,input().split()))
A = sorted(a)
k = K // N
m = A[K%N]
for i in range(N):
  print(k) if m <= a[i] else print(k + 1)
