H,W = map(int,input().split())
A = []
for i in range(H):
  A = list(map(int,input().split()))
  L = ['.' if i == 0 else chr(i+64) for i in A]
  print("".join(L))
