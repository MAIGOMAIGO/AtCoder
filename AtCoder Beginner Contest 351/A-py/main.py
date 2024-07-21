A = sum(list(map(int,input().split())))
B = sum(list(map(int,input().split())))
print(A-B+1 if A>=B else 0)