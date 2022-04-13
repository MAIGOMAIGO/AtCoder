#include <stdio.h>
int main(void){
  int A,B,C,D;
  (void)scanf("%d %d %d %d",&A,&B,&C,&D);
  printf("%s",((C+B-1)/B <= (A+D-1)/D)?"Yes":"No");
  return 0;
}
