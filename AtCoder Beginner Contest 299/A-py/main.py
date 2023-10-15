N = int(input())
S = input()
print("in" if '*' in S[S.find('|'):S.rfind('|')] else "out")
