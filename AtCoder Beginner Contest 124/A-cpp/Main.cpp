#include <iostream>
using namespace std;

int main(void){
  int A,B,C=0;
  cin >> A >> B;
  if(A>B){
    C += A;
    A--;
  }else{
    C += B;
    B--;
  }
  if(A>B)C += A;
  else C += B;
  cout << C << endl;
  return 0;
}
