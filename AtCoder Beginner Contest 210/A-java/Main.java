import java.util.Scanner;
class Main{
  public static void main(String[] args){
    var scan = new Scanner(System.in);
    int N = scan.nextInt();
    int A = scan.nextInt();
    int X = scan.nextInt();
    int Y = scan.nextInt();
    if(N <= A){
      System.out.println(N*X);
    }else{
      System.out.println(A*X+(N-A)*Y);
    }
  }
}
