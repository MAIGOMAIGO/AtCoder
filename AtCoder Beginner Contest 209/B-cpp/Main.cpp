#include <iostream>
using namespace std;
int main(){
  int N,X;
  cin >> N >> X;
  for(int i=1;i<=N;i++){
    int A;
    cin >> A;
    if(i%2==0){
      X -= A-1;
    }else{
      X -= A;
    }
    if(X < 0){
      cout << "No" << endl;
      return 0;
    }
  }
  cout << "Yes" << endl;
  return 0;
}
