N,M,D = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
n,m = 0,0
for i in range(N+M):
  if D >= abs(A[n]-B[m]):
    print(A[n]+B[m])
    exit(0)
  else:
    if A[n] > B[m]:
      n += 1
    else:
      m += 1
    if n >= N or m >= M:
      break
print(-1)
