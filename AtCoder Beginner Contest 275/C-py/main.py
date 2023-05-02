S = []
for i in range(9):
  S.append(input())
c = 0
for H in range(9):
  for W in range(9):
    if S[H][W] == '#':
      for i in range(9-H):
        for j in range(1,9-W):
          if H+i+j < 9 and W-i >= 0:
            if S[H+i][W+j]=='#' and S[H+j][W-i]=='#' and S[H+i+j][W+j-i]=='#':
              c += 1
print(c)
