R,C = map(int,input().split())
B = []
for i in range(R):
  B.append(input())
S = ""
for i in range(R*C):
  if B[i//C][i%C] == "#":
    for j in range(R*C):
      if B[j//C][j%C] != "#" and B[j//C][j%C] != ".":
        if abs(j//C - i//C) + abs(j%C - i%C) <= int(B[j//C][j%C]):
          S += "."
          break
    if len(S) != i+1:
      S += "#"
  else:
    S += "."
for i in range(R):
  print(S[i*C:i*C+C])
