N = int(input())
A = list(map(int,input().split()))
L = [i for i in A if i%2 == 0]
print(*L)
