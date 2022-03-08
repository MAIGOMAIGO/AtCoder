import sys
A,B = map(str,input().split())
for i in range(len(A) if len(A)<=len(B) else len(B)):
  if len(str(int(A[-i-1]) + int(B[-i-1])))>=2:
    print("Hard")
    sys.exit()
print("Easy")
