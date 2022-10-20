import java.util.Scanner;
public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int K = scan.nextInt();
	int X = scan.nextInt();
    System.out.println(K*500>=X?"Yes":"No");
  }
}
