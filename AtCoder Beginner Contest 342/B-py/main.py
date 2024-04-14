N = int(input())
P = list(map(int,input().split()))
D = {P[i]:i for i in range(N)}
Q = int(input())
for i in range(Q):
  A,B = map(int,input().split())
  print(P[min(D[A], D[B])])
