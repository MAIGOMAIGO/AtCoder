N,M = map(int,input().split())
A = list(map(int,input().split()))
print(-1) if sum(A) > N else print(N-sum(A))
