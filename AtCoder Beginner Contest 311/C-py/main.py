N = int(input())
A = list(map(int,input().split()))
D = {i+1:A[i] for i in range(N)}
S = set()
for i in range(N):
  if i+1 not in S:
    s = set()
    s.add(i+1)
    j = i+1
    while(True):
      if D[j] in s:
        L = [j]
        k = j
        while(True):
          if D[k] == L[0]:
            break
          else:
            L.append(D[k])
            k = D[k]
        print(len(L))
        print(*L)
        exit(0)
      else:
        if D[j] in S:
          for k in s:
            S.add(k)
          break
        s.add(j)
        j = D[j]
