N = int(input())
for i in range(N,920):
  if ((i//100) * ((i//10)%10)) == i%10:
    print(i)
    break
