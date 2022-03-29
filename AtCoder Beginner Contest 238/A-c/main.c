#include <stdio.h>
#include <math.h>
int main(void){
  double n;
  scanf("%lf",&n);
  printf("%s",(pow(2,n)>n*n)?"Yes":"No");
  return 0;
}
