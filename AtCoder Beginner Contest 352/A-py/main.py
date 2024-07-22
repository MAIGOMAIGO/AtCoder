N,X,Y,Z = map(int,input().split())
print("Yes" if (X <= Z <= Y) or (X >= Z >= Y) else "No")