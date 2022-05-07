#include <stdio.h>
#include <string.h>
int main(void){
  char S[15];
  scanf("%s",S);
  printf("%s",strcmp(S,"Hello,World!")==0?"AC":"WA");
  return 0;
}
