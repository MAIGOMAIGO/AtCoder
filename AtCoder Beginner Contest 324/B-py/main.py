N = int(input())
while N>1:
  if N%2 == 0 or N%3 == 0:
    if N%2 == 0:
      N /= 2
    elif N%3 == 0:
      N /= 3
  else:
    break
print("Yes" if N == 1 else "No") 
