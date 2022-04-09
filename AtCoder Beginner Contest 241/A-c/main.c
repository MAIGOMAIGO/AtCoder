#include <stdio.h>
int main(void){
  int a[10];
  for(int i=0;i<10;i++){
    (void)scanf("%d",&a[i]);
  }
  int k=0;
  for(int i=1;i<3;i++){
    k = a[k];
  }
  printf("%d",a[k]);
  return 0;
}
