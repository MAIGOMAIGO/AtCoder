# AtCoder Regular Contest 111 A Simple Math 2  
https://atcoder.jp/contests/arc111/tasks/arc111_a  
Python (3.8.2)で回答  

最初に`(10**N)//M%M`で計算したらTLEだった。  
どうしたものかと解説をみたら`10**N`ではなく`pow()`を使い計算していた。  
式変形は解説にあるものの、powを第三引数まで使うことで早くなる理由が無いので調べた。  
https://himibrog.com/python-pow/  
上のリンクからわかる通り公式がpow関数で第三引数を使い余りを出した方が早いとあった。  
そのため、今回の問題の制限時間に間に合う。
