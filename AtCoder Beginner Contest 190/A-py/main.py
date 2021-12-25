N = list(map(int, input().split()))
if N[2] == 0:
  if N[1] >= N[0]:
    print("Aoki")
  else:
    print("Takahashi")
else:
  if N[0] >= N[1]:
    print("Takahashi")
  else:
    print("Aoki")
