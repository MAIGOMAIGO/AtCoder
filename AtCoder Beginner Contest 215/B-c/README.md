# AtCoder Beginner Contest 215 B log2(N)  
https://atcoder.jp/contests/abc215/tasks/abc215_b  
C (GCC 9.2.1)で回答  

2^k <= Nとなる時、2進数で考えるとNはk+1桁であると考えられる。  
そのためNが2進数で何桁か計算した。  
左からN(2)を見ていき、最初に1が表示された桁数-1が答えである。
