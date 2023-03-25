N = int(input())
A = list(map(int,input().split()))
m1,m2 = -1,-1
m3,m4 = -1,-1
for a in A:
  if a%2 == 0:
    if min(m1,m2) < a:
      if m1 > m2:
        m2 = a
      else:
        m1 = a
  else:
    if min(m3,m4) < a:
      if m3 > m4:
        m4 = a
      else:
        m3 = a
if (m1 != -1) and (m2 != -1) and (m3 != -1) and (m4 != -1):
  print(max(m1+m2,m3+m4))
elif (m1 != -1) and (m2 != -1):
  print(m1+m2)
elif (m3 != -1) and (m4 != -1):
  print(m3+m4)
else:
  print(-1)
