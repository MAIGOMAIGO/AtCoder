W,B = map(int,input().split())
S = "wbwbwwbwbwbw" * 22
for i in range(220 - (W+B)):
  s = S[i:i+W+B]
  if s.count("w") == W:
    print("Yes")
    exit(0)
print("No")