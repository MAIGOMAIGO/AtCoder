# AtCoder Beginner Contest 216 C Many Balls  
https://atcoder.jp/contests/abc216/tasks/abc216_c  
Java (OpenJDK 11.0.6)で回答  

魔法をどのように使えばピッタリになるか考えたところ、時を戻せばいいのだと気付いた。  
整数Nが偶数ならその前に魔法Bを使ってるだろうし、奇数なら必ず魔法Aを使ったことになる。  
つまり逆から計算していき、出来た文字列を再度ひっくり返せば使うべき魔法の順番がわかる。  

ということをPythonでやろうとしたら失敗したのでJavaで作った。
