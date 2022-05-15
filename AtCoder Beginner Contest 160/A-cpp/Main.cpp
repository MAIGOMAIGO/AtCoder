#include <iostream>
#include <string>
using namespace std;

int main(void){
  string S;cin >> S;
  S = S[2]==S[3]&&S[4]==S[5]?"Yes":"No";
  cout << S << endl;
  return 0;
}
