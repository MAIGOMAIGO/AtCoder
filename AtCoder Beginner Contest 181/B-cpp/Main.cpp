#include <iostream>
using namespace std;
int main(void){
  double A,B,N;
  long X=0;
  cin >> N;
  for(int i=0;i<N;i++){
    cin >> A >> B;
    X = X + (B-A+1)*((A+B)/2);
  }
  cout << X << endl;
  return 0;
}
