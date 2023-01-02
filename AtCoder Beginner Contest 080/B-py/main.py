N = input()
L = [int(N[i]) for i in range(len(N))]
print("Yes") if int(N)%sum(L) == 0 else print("No")
