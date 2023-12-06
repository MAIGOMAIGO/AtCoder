S = list(map(int,input().split()))
for i in range(7):
  if S[i] > S[i+1] or S[i] < 100 or S[i] > 675 or S[i]%25 != 0:
    print("No")
    exit(0)
if 100 <= S[7] <= 675 and S[7]%25 == 0:
  print("Yes")
else:
  print("No")
