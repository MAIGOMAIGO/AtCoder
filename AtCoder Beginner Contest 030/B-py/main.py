n,m = map(int,input().split())
nd = n%12/12*360+m/60*30
md = m/60*360
print(min(abs(nd-md),360-abs(nd-md)))
