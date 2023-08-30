#include <iostream>
int cou_n(int n){
  int c = 0,i = 1;
  while(i*i <= n){
    if(n%i == 0){
      c++;
      if(i != n/i)c++;
    }
    i++;
  }
  return c;
}

int main(void){
  int N;
  std::cin >> N;
  long long c = 0;
  for(int i=1;i<N;i++){
    int d1 = cou_n(N-i);
    if(i == N-i) c += d1*d1;
    else if(i > N-i)break;
    else{
      int d2 = cou_n(i);
      c += 2 * d1 * d2;
    }
  }
  std::cout << c << std::endl;
  return 0;
}
