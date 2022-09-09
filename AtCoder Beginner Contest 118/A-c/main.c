#include <stdio.h>
int main(void){
  int A,B;
  scanf("%d %d",&A,&B);
  printf("%d",B%A==0?A+B:B-A);
  return 0;
}
