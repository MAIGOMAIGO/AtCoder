A,B,C = map(int,input().split())
print('?') if A+B == A-B == C else print('+') if A+B == C else print('-') if A-B == C else print('!')
