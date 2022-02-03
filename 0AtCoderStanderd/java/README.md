## 標準
```java
import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
    }
}
```

## 標準入力

```java
// S 文字列 1行
String S = scan.nextLine();
// N 整数 1行
int N = Integer.parseInt(scan.nextLine());
// N M 整数 半角までを入力
int N = scan.nextInt();
int M = scan.nextInt();
```

## 標準出力

```java
System.out.println("なんか書いとけ");
```

## 良く使うやり方

```java
// 文字列の切り出し
// String.substring(切り始め,切り終わり);
String S = "open";
System.out.println(S.substring(1,4); // pen
System.out.println(S.substring(0,2); // op
// 文字の取得
System.out.println(S.charAt(1); // char型 p
// 文字の比較 ==では違う判定にされるので注意
String str = "open";
S.equals(str); // True
```
