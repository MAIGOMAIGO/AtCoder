X,K = map(int,input().split())
for i in range(K):
  if (X // (10**(i)))%10 >= 5:
    X = -(-X // (10**(i+1))) * (10**(i+1))
  else:
    X = (X // (10**(i+1))) * (10**(i+1))
print(X)
