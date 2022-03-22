#include <stdio.h>
int main(void){
  int N;
  char S[5000];
  scanf("%d %s",&N,S);
  int c = 0;
  for(int i=0;i<N;i++){
    int at=0,cg=0;
    for(int k=i;k<N;k++){
      if(S[k] == 'A'){
        at++;
      }else if(S[k] == 'T'){
        at--;
      }else if(S[k] == 'C'){
        cg++;
      }else{
        cg--;
      }
      if(at == 0 && cg == 0){
        c++;
      }
    }
  }
  printf("%d",c);
  return 0;
}
