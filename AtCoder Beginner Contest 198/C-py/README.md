# AtCoder Beginner Contest 198 C Compass Walking  
https://atcoder.jp/contests/abc198/tasks/abc198_c  
Python (3.8.2)で回答  

Zは座標(X,Y)までの距離を表しており、Rも一度に動ける距離を表しているので一次元的な動きになる。
Zの長さがRと同一なら1回、ZがRより短いなら2回、ZがRより大きく割り切れるならZ/R、割り切れないならZ/R+1である。
