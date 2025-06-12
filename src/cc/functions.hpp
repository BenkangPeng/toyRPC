#ifndef CC_FUNCTIONS_HPP
#define CC_FUNCTIONS_HPP

#include <vector>

std::vector<int> prim(int n);

std::vector<int> fib(int n);

std::vector<std::vector<int>> matrixMul(std::vector<std::vector<int>> &A,
                                        std::vector<std::vector<int>> &B);

#endif