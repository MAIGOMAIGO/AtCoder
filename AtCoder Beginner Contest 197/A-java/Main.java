import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String s = scan.nextLine();
    System.out.println(s.substring(1,3)+s.substring(0,1));
  }
}
