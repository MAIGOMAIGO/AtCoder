# AtCoder Regular Contest 102 C Triangular Relationship  
https://atcoder.jp/contests/arc102/tasks/arc102_a  
C (GCC 9.2.1)で回答  

a+b,b+c,c+aがそれぞれKの倍数である時を二つに分けた。一つ目はa%K=b%K=c%K=0の時。二つ目はa%K=b%K=c%K=K/2の時である。  
a%K=0の時はN/K回(少数切り捨て)起こるので、a,b,cそれぞれで(N/K)^3回Kの倍数になる。  
a%K=K/2の時ではKは必ず偶数であり、nK+K/2なので(N+K/2)/K^3回である。  
以上の回数を足したのが答えである。  


眠くて頭が回ってないのでメモ  
入力例：11 4  
11 / 4 = 2、2^3=8  
(11 + 4/2) / 4 = 3、3^3=27
27+8=35  
N以下のKの倍数の数を三乗、Kが偶数だと2a=nKが成立するからN+K/2以下でKの倍数の数を三乗、それぞれ足すと答え。  
答えが32bitじゃ足りなくなる程大きくなることもあるのでlongなどを使い計算。同じ理由でシンプルにfor回すとTLEになる。