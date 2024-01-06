N,M = map(int,input().split())
s = set([i+1 for i in range(N)])
w,l,S = set(),set(),set()
for i in range(M):
  A,B = map(int,input().split())
  S.add((A,B))
  s.discard(A)
  s.discard(B)
  if B in w:
    w.discard(B)
  l.add(B)
  if A not in l:
    w.add(A)
if len(w)==0 or len(s)>0:
  print(-1)
elif len(w)==1:
  print(list(w)[0])
else:
  print(-1)
