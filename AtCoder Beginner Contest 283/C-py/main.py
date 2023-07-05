S = input()
le = len(S)
S = S.replace("00","")
print(len(S)+(le-len(S))//2)
