N = int(input())
c = 0
for i in range(N):
  S = input()
  c += 1 if S == "For" else 0
print("Yes" if c >= N/2 else "No")
