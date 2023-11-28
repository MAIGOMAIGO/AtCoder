N = int(input())
A = list(map(int,input().split()))
L = [sum(A[(i-1)*7:i*7])for i in range(1,N+1)]
print(*L)
