#include <iostream>
#include <set>
int main(void){
  int N;
  std::cin >> N;
  std::set<int> a;
  for(int i=0;i<N;i++){
    int A;
    std::cin >> A;
    a.insert(A);
  }
  int max = *std::max_element(a.begin(),a.end());
  int min = *std::min_element(a.begin(),a.end());
  std::cout << max-min << std::endl;
  return 0;
}
