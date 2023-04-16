abc = list(map(int,input().split()))
print("Yes") if sum(abc) - max(abc) == max(abc) else print("No")
