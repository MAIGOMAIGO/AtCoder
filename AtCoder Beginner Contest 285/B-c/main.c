#include <stdio.h>
int main(void){
  int N;scanf("%d",&N);
  char S[N];scanf("%s",S);
  for(int i=1;i<N;i++){
    int c = 0;
    for(int k=0;k<N-i;k++){
      if(S[k] != S[k+i]){
        c++;
      }else{
        break;
      }
    }
    printf("%d\n",c);
  }
  return 0;
}
