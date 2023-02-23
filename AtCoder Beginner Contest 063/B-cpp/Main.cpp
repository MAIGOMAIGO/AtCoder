#include <iostream>
#include <string>
using namespace std;
int main(void){
  string S;
  cin >> S;
  for(int i=0;i<S.size()-1;i++)
    for(int j=i+1;j<S.size();j++)
      if(S[i] == S[j]){
        cout << "no" << endl;
        return 0;
      }
  cout << "yes" << endl;
  return 0;
}
