N,M = map(int,input().split())
D = [[0] for i in range(N)]
for i in range(M):
  AB = list(map(int,input().split()))
  D[AB[0]-1].append(AB[1])
  D[AB[1]-1].append(AB[0])
for i in range(N):
  D[i].sort()
  print(len(D[i])-1," ".join([str(s) for s in D[i][1:]]))
