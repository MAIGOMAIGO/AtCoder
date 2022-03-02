S = input()
L = [S[i:]+S[0:i] for i in range(len(S))]
L.sort()
print(L[0])
print(L[-1])
