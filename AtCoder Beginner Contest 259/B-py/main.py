import math

a,b,d = map(int,input().split())
ad = math.cos(math.radians(d))*a - math.sin(math.radians(d))*b
bd = math.cos(math.radians(d))*b + math.sin(math.radians(d))*a
print(ad,bd)
