S = input()
print("Yes" if S[0].isupper() and (S[1:].islower() or len(S) < 2) else "No")
