A,B,K = map(int,input().split())
L = [i for i in range(A,A+K)] + [i for i in range(B-K+1,B+1)]
L = sorted(list(set(L)))
for i in L:
  if A <= i <=B:
    print(i)
