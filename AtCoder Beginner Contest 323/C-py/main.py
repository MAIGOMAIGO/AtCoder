N,M = map(int,input().split())
A = list(map(int,input().split()))
L = [i+1 for i in range(N)]
D = {i+1:list() for i in range(N)}
for i in range(N):
  S = input()
  for j in range(M):
    if S[j] == "o":
      L[i] += A[j]
    else:
      D[i+1].append(A[j])
  D[i+1].sort(reverse=True)
mp = max(L)
for i in range(N):
  if L[i] == mp:
    print(0)
  else:
    c = 0
    for j in D[i+1]:
      L[i] += j
      c += 1
      if L[i] >= mp:
        print(c)
        break
