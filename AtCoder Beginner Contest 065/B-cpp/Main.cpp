#include <iostream>
int main(void){
  int N;
  std::cin >> N;
  int a[N];
  for(int i=0;i<N;i++)
    std::cin >> a[i];
  int p = 0;
  for(int i=0;i<N;i++){
    if(a[p] == 2){
      std::cout << i+1 << std::endl;
      return 0;
    }else{
      p = a[p]-1;
    }
  }
  std::cout << -1 << std::endl;
  return 0;
}
