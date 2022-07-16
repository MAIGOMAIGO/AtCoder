N = int(input())
L = [i for i in list(range(1,N+1)) if len(str(i))%2==1]
print(len(L))
