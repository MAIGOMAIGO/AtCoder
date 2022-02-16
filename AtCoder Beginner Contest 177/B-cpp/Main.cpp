#include<stdio.h>
#include<string.h>
int main(void){
  char S[1000],T[1000];
  scanf("%s\n%s",&S,&T);
  int a = strlen(T);
  for(int i=0;i<=strlen(S)-strlen(T);i++){
    int t=0;
    for(int k=0;k<strlen(T);k++){
      if(T[k] != S[i+k]){
        t++;
      }
    }
    a = a>t ? t:a;
  }
  printf("%d",a);
  return 0;
}
