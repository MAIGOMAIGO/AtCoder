N,K = map(int,input().split())
sunuke = []
for i in range(K):
  d = int(input())
  A = list(map(int,input().split()))
  sunuke += A
print(N-len(set(sunuke)))
