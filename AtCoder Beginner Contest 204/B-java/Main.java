import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int N = scan.nextInt();
    int a=0;
    for(int i=0;i<N;i++){
      int A = scan.nextInt();
      if(A > 10){
        a += A-10;
      }
    }
    System.out.println(a);
  }
}
