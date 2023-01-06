X,Y,N = map(int,input().split())
print((N//3)*Y + (N%3)*X) if 3*X >= Y else print(N*X)
