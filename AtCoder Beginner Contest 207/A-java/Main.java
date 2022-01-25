import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int A = scan.nextInt();
    int B = scan.nextInt();
    int C = scan.nextInt();
    if(A > B && C > B){
      System.out.println(A+C);
    }else if(A > C && B > C){
      System.out.println(A+B);
    }else{
      System.out.println(B+C);
    }
  }
}
