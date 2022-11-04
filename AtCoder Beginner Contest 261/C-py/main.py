N = int(input())
D = {}
for i in range(N):
  S = input()
  if S in D.keys():
    print(S+'('+ str(D[S]) +')')
    D[S] += 1
  else:
    print(S)
    D[S] = 1
