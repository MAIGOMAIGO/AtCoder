N = int(input())
i = 0
while True:
  if i == i&N:
    print(i)
  else:
    b = (i|N)&(~N)
    s = len(bin(b))-2
    i = i >> s
    i += 1
    i= i << s
    i -= 1
  if i > N:
    break
  else:
    i += 1
