# AtCoder Beginner Contest 138 B Resistors in Parallel  
https://atcoder.jp/contests/abc138/tasks/abc138_b  
Python (3.8.2)で回答  

式変形すると分子がAの総積で分母がi以外の値の総積の総和なのでその通り計算する。  
例：A = [10,20,30] 1/(1/10+1/20+1/30)  
変形後 (10×20×30)/(600+300+200) = 6000/1100 = 5.45454545  
