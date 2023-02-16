X,A,B = map(int,input().split())
print("delicious") if B <= A else print("safe") if B-A <= X else print("dangerous")
