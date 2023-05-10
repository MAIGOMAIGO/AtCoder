N = int(input())
P = list(map(int,input().split()))
for i in range(N):
  p = P[len(P)-1-i:]
  if p != sorted(p):
    L = [i for i in p[1:] if p[0] > i]
    S = P[:len(P)-1-i]
    m = max(L)
    S.append(m)
    p.remove(m)
    S += sorted(p,reverse=True)
    print(" ".join([str(j) for j in S]))
    break
