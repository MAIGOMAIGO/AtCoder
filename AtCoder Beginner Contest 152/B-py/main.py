a,b = map(str,input().split())
print(a*int(b)) if a*int(b) < b*int(a) else print(b*int(a))
