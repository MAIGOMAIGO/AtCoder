import re
S = input()
if S[0] == 'A':
  if S[2:len(S)-1].count('C') == 1:
    if re.sub(r'[a-z]+','',S) == 'AC':
      print('AC')
      exit(0)
print('WA')
