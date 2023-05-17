import java.util.Scanner;
import java.util.Arrays;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    String s1 = "HDCS";
    String s2 = "A23456789TJQK";
    
    int N = Integer.parseInt(scan.nextLine());
    String S[] = new String[N];
    for(int i=0;i<N;i++){
      String s = scan.nextLine();
      if( Arrays.asList(S).contains(s)
         || !s1.contains(String.valueOf(s.charAt(0)))
         || !s2.contains(String.valueOf(s.charAt(1)))){
        System.out.println("No");
        System.exit(0);
      }
      S[i] = s;
    }
    System.out.println("Yes");
  }
}
