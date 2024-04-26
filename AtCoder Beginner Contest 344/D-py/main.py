import copy
T = input()
N = int(input())
S = [input().split()[1:] for i in range(N)]
D = {T[:i]:-1 for i in range(len(T)+1)}
L = [copy.deepcopy(D) for i in range(N)]
D[""] = 0
for i in range(N):
  for j in S[i]:
    for k in D.keys():
      if D[k] != -1:
        if k + j in D:
          if D[k + j] == -1:
            L[i][k + j] = D[k]+1
          else:
            L[i][k + j] = min(D[k]+1, D[k + j])
  for j in D.keys():
    if L[i][j] != -1:
      D[j] = L[i][j]
print(D[T])
