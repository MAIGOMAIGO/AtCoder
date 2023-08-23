N = int(input())
X = list(map(int,input().split()))
X.sort()
xn = X[N:-N]
print(sum(xn)/len(xn))
