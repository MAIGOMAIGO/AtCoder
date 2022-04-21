N,A,X,Y = map(int,input().split())
print(N*X) if N <= A else print(A*X+(N-A)*Y)
