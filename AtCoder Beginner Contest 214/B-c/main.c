#include <stdio.h>
int main(){
  long S,T,X=0;
  scanf("%ld %ld",&S,&T);
  for(int a=0;a<=S;a++){
    for(int b=0;b<=S;b++){
      for(int c=0;c<=S;c++){
        if((a+b+c <= S) && (a*b*c <= T))X++;
      }
    }
  }
  printf("%ld",X);
  return 0;
}
