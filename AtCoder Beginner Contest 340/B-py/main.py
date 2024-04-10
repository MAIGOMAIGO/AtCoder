Q = int(input())
A = []
for i in range(Q):
  query = list(map(int, input().split()))
  if query[0] == 1:
    x = query[1]
    A.append(x)
  elif query[0] == 2:
    k = query[1]
    print(A[-k])
