K = int(input())
SA,SB = map(str,input().split())
A,B = 0,0
for a in range(len(SA)):
  A += int(SA[len(SA)-a-1]) * K**a
for b in range(len(SB)):
  B += int(SB[len(SB)-b-1]) * K**b
print(A*B)
