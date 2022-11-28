## 標準
```c++
#include <iostream>
int main(){
  
  return 0;
}  
```

## 標準入力

```c++
// N 整数
int N;
std::cin >> N;
```

## 標準出力

```c++
// N 整数
std::cout << N << std::endl;
```
## 集合

```c++
#include <set>
std::set<int> st{3,1,4};
// 追加
st.insert(n);
// 削除
st.erase(n);
// 検索
auto a = st.find(n);
```

## 可変長配列

```c++
#include <vector>
std::vector<int> vec(N);
// 追加
vec.push_back(n);
// 削除
vec.erase(std::cbegin(vec)+idx);
// ソート
#include <algorithm>
std::sort(data.begin(),data.end());//昇順ソート
// 最大値
int min = *std::min_element(vec.begin(), vec.end());
// 最小値
int max = *std::max_element(vec.begin(), vec.end());
```
