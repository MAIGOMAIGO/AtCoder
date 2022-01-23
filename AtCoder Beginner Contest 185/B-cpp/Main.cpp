#include <iostream>
using namespace std;
int main(){
  int N,M,T;
  cin >> N >> M >> T;
  int n = N;
  int A[M],B[M];
  for(int i=0;i<M;i++){
    cin >> A[i] >> B[i];
    if(i == 0){
      n -= A[i];
    }else{
      n -= (A[i] - B[i-1]);
    }
    if(n<=0){
      cout << "No" << endl;
      return 0;
    }
    n += (B[i] - A[i]);
    if(n > N)n = N;
  }
  if(n - (T-B[M-1]) <= 0){
    cout << "No" << endl;
  }else{
    cout << "Yes" << endl;
  }
  return 0;
}  
