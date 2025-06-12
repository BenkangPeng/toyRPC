#include "functions.hpp"

std::vector<int> prim(int n){
    if (n <= 0) return {};
    if (n == 1) return {2};
    
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

std::vector<int> fib(int n){
    std::vector<int> res(n);
    res[0] = 1;
    res[1] = 1;
    for(int i = 2; i < n; ++i){
        res[i] = res[i-1] + res[i-2];
    }

    return res;
}