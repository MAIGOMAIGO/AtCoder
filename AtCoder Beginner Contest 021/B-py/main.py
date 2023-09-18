N = int(input())
a,b = map(int,input().split())
K = int(input())
P = list(map(int,input().split()))
if len(set(P)) == len(P) and a not in P and b not in P:
  print("YES")
else:
  print("NO")
