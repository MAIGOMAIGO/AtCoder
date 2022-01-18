#include <stdio.h>
int main(){
  int N;
  scanf("%d", &N);
  int A[N];
  for(int i=0;i<N;i++){
    scanf("%d", &A[i]);
  }
  for(int i=0;i<N;i++){
    for(int l=0;l<N-i-1;l++){
      if(A[l] > A[l+1]){
        int a = A[l];
        A[l] = A[l+1];
        A[l+1] = a;
      }
    }
    if(N-i != A[N-i-1]){
      printf("No");
      return 0;
    }
  }
  printf("Yes");
  return 0;
}
