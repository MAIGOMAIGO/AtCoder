#include <stdio.h>
int main(void){
  double A,B;
  scanf("%lf %lf",&A,&B);
  printf("%lf",(A-B)/A*100);
  return 0;
}
