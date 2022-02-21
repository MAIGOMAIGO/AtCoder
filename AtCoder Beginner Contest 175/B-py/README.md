# AtCoder Beginner Contest 175 B Making Triangle  
https://atcoder.jp/contests/abc175/tasks/abc175_b  
Python (3.8.2)で回答  

三角形の3辺の長さについて以下の定理が成り立つ  
1.三角形の2辺の長さの和は、他の1辺の長さより大きい。  
2.三角形の2辺の長さの差は、他の1辺の長さより小さい。  
そのためソートされた配列Lの中から、同じ長さの辺を使わずにi,j,kを選びそれらが上記の条件を満たしている回数を数える。  
Nは100以下のため全探索できる。
