# include <stdio.h>
#define MIN(a,b) a<b?a:b
int main(void){
  int A,B,C,D;
  scanf("%d\n%d\n%d\n%d",&A,&B,&C,&D);
  printf("%d",(MIN(A,B)) + (MIN(C,D)));
  return 0;
}
