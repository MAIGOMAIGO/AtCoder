N,W = map(int,input().split())
A = list(map(int,input().split()))
L1,L2,L3 = [],[],[]
for i in range(N):
  if A[i] <= W:
    L1.append(A[i])
    for j in range(i+1,N):
      if A[i]+A[j] <= W:
        L2.append(A[i]+A[j])
        for k in range(j+1,N):
          if A[i]+A[j]+A[k] <= W:
            L3.append(A[i]+A[j]+A[k])
L1.extend(L2)
L1.extend(L3)
L1 = list(set(L1))
print(len(L1))
