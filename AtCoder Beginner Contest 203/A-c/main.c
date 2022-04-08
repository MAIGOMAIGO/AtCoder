#include <stdio.h>
int main(void){
  int a,b,c;
  scanf("%d %d %d",&a,&b,&c);
  if(a==b){
    printf("%d",c);
  }else if(b==c){
    printf("%d",a);
  }else if(a==c){
    printf("%d",b);
  }else{
    printf("0");
  }
  return 0;
}
