S,P = map(int,input().split())
for i in range(1,int(P**0.5)+1):
  if P%i == 0:
    if P/i + i == S:
      print("Yes")
      exit(0)
print("No")
