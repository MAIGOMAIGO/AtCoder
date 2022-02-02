# AtCoder Beginner Contest 183 B Billiards  
https://atcoder.jp/contests/abc183/tasks/abc183_b  
Python (3.8.2)で回答  

入射角及び反射角が同じになる反射点は比で求まる。  
反射点を仮にPとするとPx-Sx:Gx-Px = Sy:Gyになるので、Sy/(Gy+Sy)=Sx/(Gx+Sx)である。  
そのため((Gx-Sx) * Sy / (Gy+Sy))に基準点のSxを足すことで答えが求められる。
