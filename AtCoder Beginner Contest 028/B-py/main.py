D = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0}
S = input()
for i in range(len(S)):
  D[S[i]] += 1
print(D['A'],D['B'],D['C'],D['D'],D['E'],D['F'])
