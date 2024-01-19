M = int(input())
D = list(map(int,input().split()))
Y = -(-sum(D)//2)
for i in range(M):
  if D[i] >= Y:
    print(i+1,Y)
    exit(0)
  else:
    Y -= D[i]
