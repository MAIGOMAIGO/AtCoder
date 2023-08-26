A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
print((A-C)*S+(B-C)*T) if S+T >= K else print(A*S+B*T)
