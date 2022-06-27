N = int(input())
d = list(map(int,input().split()))
L = []
for i in range(N-1):
  for j in range(i+1,N):
    L.append(d[i]*d[j])
print(sum(L))
