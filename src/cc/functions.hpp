#ifndef CC_FUNCTIONS_HPP
#define CC_FUNCTIONS_HPP

#include <vector>

std::vector<int> prim(int n);

std::vector<int> fib(int n);

std::vector<std::vector<int>> matmul(std::vector<std::vector<int>> &A,std::vector<std::vector<int>> &B);

class matrix {
public:
  matrix();
  std::vector<std::vector<int>> mul(std::vector<std::vector<int>> &A,
                                    std::vector<std::vector<int>> &B);

  std::vector<std::vector<int>> transpose(std::vector<std::vector<int>> &A);
};

#endif