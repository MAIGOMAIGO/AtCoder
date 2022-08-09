import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int N = Integer.parseInt(scan.nextLine());
    System.out.println(N%2==0?"White":"Black");
  }
}
