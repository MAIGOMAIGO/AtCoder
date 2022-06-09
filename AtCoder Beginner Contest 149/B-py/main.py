A,B,K = map(int,input().split())
if A >= K:
  A -= K
  K = 0
else:
  K -= A
  A = 0
  B = 0 if B <= K else B-K
print(A,B)
