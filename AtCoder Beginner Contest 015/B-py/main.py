N = int(input())
A = list(map(int,input().split()))
A = [i for i in A if i != 0]
print(-(-sum(A)//len(A)))
