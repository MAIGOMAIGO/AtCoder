
# AtCoder Beginner Contest 190 D Staircase Sequences  
https://atcoder.jp/contests/abc190/tasks/abc190_d  
Python (3.8.2)で回答  

等差数列の参考URL  
https://www.kwansei.ac.jp/hs/z90010/sugakua/suuretu/tousasum/tousasum.htm  

等差数列の和と公差は分かっているので、項数を1から2×Nまで試し、初項が整数である回数が答え。  
しかし、Nが最大で10^12まであるため時間が間に合わない。  
時短のために、2×Nの約数だけを試す。(詳しくは解説を参照してください。)  
初項が正の整数であるときだけをカウントし、カウント結果を2倍にして出力すると答えと同じになる。
