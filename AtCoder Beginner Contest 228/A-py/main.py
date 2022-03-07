S,T,X = map(int,input().split())
if S<T:
  print("Yes") if S<=X and X<T else print("No")
else:
  print("Yes") if S<=X or X<T else print("No")
