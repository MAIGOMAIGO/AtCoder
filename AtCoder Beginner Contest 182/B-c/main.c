#include <stdio.h>
int main(void){
  int N;
  scanf("%d",&N);
  int A[N];
  for(int i=0;i<N;i++){
    scanf("%d",&A[i]);
  }
  int t[2] = {0,0};
  for(int k=2;k<=1000;k++){
    int p=0;
    for(int i=0;i<N;i++){
      if(A[i]%k == 0){
        p++;
      }
    }
    if(p >= t[1]){
      t[0] = k;
      t[1] = p;
    }
  }
  printf("%d",t[0]);
  return 0;
}
