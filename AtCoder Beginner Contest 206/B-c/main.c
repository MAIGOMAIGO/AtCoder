#include <stdio.h>
int main(){
  int N,i=0;
  scanf("%d",&N);
  while(N>0){
    i++;
    N -= i;
  }
  printf("%d",i);
  return 0;
}
