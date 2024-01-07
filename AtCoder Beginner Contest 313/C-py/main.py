N = int(input())
A = list(map(int,input().split()))
if 0 < sum(A)%N:
  avg1 = sum(A)//N
  avg2 = avg1 + 1
  c1 = 0
  c2 = 0
  for i in A:
    if avg1 > i:
      c1 += avg1-i
    elif avg2 < i:
      c2 += i-avg2
  c = c1+c2
  print(c//2+1 + (max(c1,c2)-min(c1,c2))//2) if c%2 == 1 else print(c//2+ (max(c1,c2)-min(c1,c2))//2)
else:
  avg = sum(A)//N
  c1 = 0
  c2 = 0
  for i in A:
    if avg > i:
      c1 += avg-i
    elif avg < i:
      c2 += i-avg
  c = c1+c2
  print(c//2+1 + (max(c1,c2)-min(c1,c2))//2) if c%2 == 1 else print(c//2+ (max(c1,c2)-min(c1,c2))//2)
