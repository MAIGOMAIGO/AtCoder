a,b = map(int,input().split())
L = [i for i in range(b-a+1)]
print(sum(L)-b)
