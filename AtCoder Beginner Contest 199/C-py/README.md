# AtCoder Beginner Contest 199 C IPFL  
https://atcoder.jp/contests/abc199  
Python (3.8.2)で回答  

今回の問題ではSをstrで受け取るとT==2の時に入れ替えがかなり時間がかかったので、Sをlistで受け取り入れ替えをしてからstrに戻した。
strで時間がかかるのは解説から考えるに、文字列の入れ替えの場合１文字ずつ行われるので時間がかかる。  
必要なところだけを入れ替えるのであれば、listの方が都合がいいようである。
