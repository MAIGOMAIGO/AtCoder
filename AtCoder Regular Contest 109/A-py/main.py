a,b,x,y = map(int,input().split())
X = 2*x*(b-a)+x if a <= b else 2*x*(a-b-1)+x
Y = (b-a)*y+x if a <= b else (a-b-1)*y+x
print(X) if X < Y else print(Y)
