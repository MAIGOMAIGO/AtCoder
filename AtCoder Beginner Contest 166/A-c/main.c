#include <stdio.h>
#include <string.h>
int main(void){
  char S[3];
  scanf("%s",S);
  printf("%s",strcmp(S,"ABC")==0?"ARC":"ABC");
  return 0;
}
