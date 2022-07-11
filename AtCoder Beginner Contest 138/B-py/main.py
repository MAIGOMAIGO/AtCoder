import math
N = int(input())
A = list(map(int,input().split()))
x = math.prod(A)
L = [x/i for i in A]
y = sum(L)
print(x/y)
