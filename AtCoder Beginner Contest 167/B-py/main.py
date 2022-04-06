A,B,C,K = map(int,input().split())
X = 0
if K > A:
  X += A
  K -= A
  if K > B:
    K -= B
    if K > 0:
      X -= K
else:
  X += K
print(X)
