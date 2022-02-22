#include <stdio.h>
#include <string.h>
int main(){
  char T[3] = "oxx";
  char S[10];
  scanf("%s",S);
  if(strlen(S) == 1){
    printf("Yes");
    return 0;
  }
  int s=0;
  if(S[0]!=S[1]){
    s = S[0] == 'o' ? 0:2;
  }else{
    s = S[0] == 'o' ? -1:1;
    if(s==-1){
      printf("No");
      return 0;
    }
  }
  for(int i=0;i<strlen(S);i++){
    if(S[i] != T[(s+i)%3]){
      printf("No");
      return 0;
    }
  }
  printf("Yes");
  return 0;
}
