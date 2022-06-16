S = input()
SR = S[::-1]
count = 0
for i in range(len(S)//2):
  if S[i] != SR[i]:
    count += 1
print(count)
