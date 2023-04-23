S = {'a':"",'b':"",'c':""}
S['a'] = input()
S['b'] = input()
S['c'] = input()
c = 'a'
for i in range(len(S['a']+S['b']+S['c'])):
  if len(S[c]) < 1:
    print(c.upper())
    break
  S[c],c = S[c][1:],S[c][0]
