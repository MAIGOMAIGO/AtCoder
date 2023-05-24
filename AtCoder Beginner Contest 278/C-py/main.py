N,Q = map(int,input().split())
S = set()
for i in range(Q):
  T,A,B = map(int,input().split())
  if T == 1:
    S.add((A,B))
  elif T == 2:
    S.discard((A,B))
  elif T == 3:
    print("Yes") if (A,B) in S and (B,A) in S else print("No")
