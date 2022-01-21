#include <iostream>
#include <cmath>
using namespace std;
int main(){
  int N;
  cin >> N;
  float X[N],Y[N];
  int t=0;
  for(int i=0;i<N;i++){
    cin >> X[i] >> Y[i];
    for(int l=0;l<i;l++){
      if(abs((Y[l]-Y[i])/(X[l]-X[i])) <= 1)t++;
    }
  }
  cout << t << endl;
  return 0;
}
