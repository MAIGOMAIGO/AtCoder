#include <stdio.h>
int main(void){
  long N,K,n;
  scanf("%ld %ld",&N,&K);
  n = N/K;
  n = n*n*n;
  if(K%2==0){
    long x = (N+K/2)/K;
    n = n + x*x*x;
  }
  printf("%ld",n);
  return 0;
}
