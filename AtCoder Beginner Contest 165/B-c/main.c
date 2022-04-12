#include <stdio.h>
int main(void){
  unsigned long X;
  (void)scanf("%lu",&X);
  unsigned long m = 100;
  int y = 0;
  while(X>m){
    m = m+m/100;
    y++;
  }
  printf("%d",y);
}
