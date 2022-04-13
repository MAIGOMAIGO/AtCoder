#include <stdio.h>
int main(void){
  int S,W;
  (void)scanf("%d %d",&S,&W);
  printf("%s",S>W?"safe":"unsafe");
  return 0;
}
