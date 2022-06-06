N = int(input())
S = input()
if "ABC" in S:
  S = S.replace("ABC","")
print((N-len(S))//3)
