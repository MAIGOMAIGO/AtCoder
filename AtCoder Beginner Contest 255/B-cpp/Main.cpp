#include <stdio.h>
#include <math.h>

int main(void){
  int N,K;scanf("%d %d",&N,&K);
  int A[K];
  for(int i=0;i<K;i++){
    scanf("%d",&A[i]);
  }
  int X[N],Y[N];
  for(int i=0;i<N;i++){
    scanf("%d %d",&X[i],&Y[i]);
  }
  unsigned long R = 0;
  for(int i=0;i<N;i++){
    int flag = 1;
    for(int j=0;j<K;j++){
      if(i+1 == A[j]){
        flag=0;
        break;
      }
    }
    if(flag){
      unsigned long a = -1;
      for(int j=0;j<K;j++){
        long long dx = X[A[j]-1]-X[i];
        long long dy = Y[A[j]-1]-Y[i];
        if(a > dx*dx + dy*dy){
          a = dx*dx + dy*dy;
        }
      }
      if(R < a)R = a;
    }
  }
  printf("%lf",sqrt(R));
  return 0;
}
