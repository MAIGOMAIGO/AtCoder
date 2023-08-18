N,K = map(int,input().split())
A = set(list(map(int,input().split())))
for i in range(K+1):
  if K != i and i not in A:
    print(i)
    break
  elif K == i:
    print(K)
