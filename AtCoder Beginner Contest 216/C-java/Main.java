import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    long N = Long.parseLong(scan.nextLine());
    String S = new String();
    while(N>0){
      if(N%2==1){
        S+="A";
        N--;
      }else{
        S+="B";
        N /= 2;
      }
    }
    StringBuilder strb = new StringBuilder(S);
    S = strb.reverse().toString();
    System.out.println(S);
  }
}
