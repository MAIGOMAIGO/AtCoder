N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
Z = [i for i in range(X+1,Y+1)]
for i in Z:
  if max(x) < i <= min(y):
    print("No War")
    exit(0)
print("War")
