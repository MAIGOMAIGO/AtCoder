#include <iostream>
using namespace std;
int main(void){
  int N,M;
  cin >> N >> M;
  int t[N] = {};
  for(int i=0;i<M;i++){
    int a,b;
    cin >> a >> b;
    t[a-1]++;
    t[b-1]++;
  }
  for(int i=0;i<N;i++){
    cout << t[i] << endl;
  }
  return 0;
}
