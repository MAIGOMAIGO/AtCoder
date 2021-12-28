NX = list(map(int, input().split()))
A = list(map(int, input().split()))
A = [str(a) for a in A if a != NX[1]]
A = " ".join(A)
print(A)
