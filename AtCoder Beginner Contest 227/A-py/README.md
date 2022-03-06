# AtCoder Beginner Contest 227 A Last Card  
https://atcoder.jp/contests/abc227/tasks/abc227_a  
Python (3.8.2)で回答  

まずAが無く毎回1から始まると考えると(K-1)%N+1である  
ここにAを入れるので(K+A-1-1)%N+1が答え
