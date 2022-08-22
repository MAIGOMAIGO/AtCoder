import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int S = scan.nextInt();
    int T = scan.nextInt();
    int X = scan.nextInt();
    if(S<T){
      System.out.println(S<=X&&X<T?"Yes":"No");
    }else{
      System.out.println(S<=X||X<T?"Yes":"No");
    }
  }
}
