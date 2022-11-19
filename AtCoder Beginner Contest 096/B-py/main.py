ABC = list(map(int,input().split()))
K = int(input())
print(sum(ABC)-max(ABC) + max(ABC)*(2**K))
