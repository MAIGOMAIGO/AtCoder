import java.util.Scanner;

public class Main{
  public static void main(String[] args){
    Scanner scan = new Scanner(System.in);
    int N = scan.nextInt();
    String[] S = new String[N];
    int[] T = new int[N];
    for(int i=0;i<N;i++){
      S[i] = scan.next();
      T[i] = scan.nextInt();
    }
    for(int i=0;i<2;i++){
      for(int l=N-1;l>0;l--){
        if(T[l] > T[l-1]){
          int t = T[l];
          String s = S[l];
          T[l] = T[l-1];
          S[l] = S[l-1];
          T[l-1] = t;
          S[l-1] = s;
        }
      }
    }
    System.out.println(S[1]);
  }
}
