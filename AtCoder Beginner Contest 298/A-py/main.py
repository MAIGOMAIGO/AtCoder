N = int(input())
S = input()
print("Yes" if S.count('x') == 0 and S.count('o') >= 1 else "No")
