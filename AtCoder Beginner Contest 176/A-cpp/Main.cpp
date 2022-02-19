#include <iostream>
int main(void){
  int N,X,T;
  std::cin >> N >> X >>T;
  std::cout << T*((N+X-1)/X);
}
