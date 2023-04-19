H,W = map(int,input().split())
C = []
for i in range(H):
  C.append(input())
c = ""
for i in range(W):
  L = [C[j][i] for j in range(H)]
  c += str(L.count("#"))
  c += " "
print(c)
