#include <stdio.h>
int main(void){
  char S[10];
  int A,B;
  scanf("%s\n%d %d",S,&A,&B);
  char s = S[A-1];
  S[A-1] = S[B-1];
  S[B-1] = s;
  printf("%s",S);
}
