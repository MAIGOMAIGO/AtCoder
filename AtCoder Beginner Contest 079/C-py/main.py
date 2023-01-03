ABCD = input()
A = int(ABCD[0])
B = int(ABCD[1])
C = int(ABCD[2])
D = int(ABCD[3])
for i in range(8):
  X = A
  X += B if i&1 == 1 else -B
  X += C if (i>>1)&1 == 1 else -C
  X += D if (i>>2)&1 == 1 else -D
  if X == 7:
    op1 = '+' if i&1 == 1 else '-'
    op2 = '+' if (i>>1)&1 == 1 else '-'
    op3 = '+' if (i>>2)&1 == 1 else '-'
    print(str(A)+op1+str(B)+op2+str(C)+op3+str(D)+"=7")
    break
