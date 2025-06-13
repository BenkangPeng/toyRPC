#include "functions.hpp"
#include <stdexcept>
#include <vector>
std::vector<int> prim(int n) {
  if (n <= 0)
    return {};
  if (n == 1)
    return {2};

  // calculate the upper bound of the n-th prime numbers
  int upper = static_cast<int>(n * (log(n) + log(log(n)))) + 10;

  std::vector<bool> sieve(upper + 1, true);
  sieve[0] = sieve[1] = false;

  for (int p = 2; p * p <= upper; p++) {
    if (sieve[p]) {
      for (int i = p * p; i <= upper; i += p) {
        sieve[i] = false;
      }
    }
  }

  std::vector<int> primes;
  primes.reserve(n);
  for (int i = 2; primes.size() < static_cast<size_t>(n) && i <= upper; i++) {
    if (sieve[i]) {
      primes.push_back(i);
    }
  }

  return primes;
}

std::vector<int> fib(int n) {
  std::vector<int> res(n);
  res[0] = 1;
  res[1] = 1;
  for (int i = 2; i < n; ++i) {
    res[i] = res[i - 1] + res[i - 2];
  }

  return res;
}

std::vector<std::vector<int>> matmul(std::vector<std::vector<int>> &A,
                                     std::vector<std::vector<int>> &B) {
  if (A.empty() || B.empty() || A[0].size() != B.size()) {
    throw std::invalid_argument(
        "Invalid matrix dimensions for multiplication.");
  }
  std::vector<std::vector<int>> res(A.size(), std::vector<int>(B[0].size(), 0));

  for (int i = 0; i < A.size(); ++i) {
    for (int j = 0; j < B[0].size(); ++j) {
      for (int k = 0; k < B.size(); ++k) {
        res[i][j] += A[i][k] * B[k][j];
      }
    }
  }
  return res;
}

std::vector<std::vector<int>> matrix::mul(std::vector<std::vector<int>> &A,
                                          std::vector<std::vector<int>> &B) {
  if (A.empty() || B.empty() || A[0].size() != B.size()) {
    throw std::invalid_argument(
        "Invalid matrix dimensions for multiplication.");
  }
  std::vector<std::vector<int>> res(A.size(), std::vector<int>(B[0].size(), 0));

  for (int i = 0; i < A.size(); ++i) {
    for (int j = 0; j < B[0].size(); ++j) {
      for (int k = 0; k < B.size(); ++k) {
        res[i][j] += A[i][k] * B[k][j];
      }
    }
  }

  return res;
}

matrix::matrix() {}

std::vector<std::vector<int>>
matrix::transpose(std::vector<std::vector<int>> &A) {
  if (A.empty()) {
    throw std::invalid_argument("Invalid matrix dimensions for transpose.");
  }
  int row = A.size();
  int col = A[0].size();
  std::vector<std::vector<int>> res(col, std::vector<int>(row, 0));

  for (int i = 0; i < row; ++i) {
    for (int j = 0; j < col; ++j) {
      res[j][i] = A[i][j];
    }
  }

  return res;
}