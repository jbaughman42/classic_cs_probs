"""
c1_fibonacci
Created October 28, 2019 by Jennifer Baughman

Description:
"""

from functools import lru_cache

memo = {0: 0, 1: 1}


def fib_recurs(n: int) -> int:
    """Basic recursive solution to Fibonacci sequence
    
    :param n: the nth number in the Fibonacci sequence
    :return: the value of the nth number in the Fibonacci sequence
    """
    if n < 2:
        return n
    else:
        return fib_recurs(n - 2) + fib_recurs(n - 2)


def fib_memo(n: int) -> int:
    """Memoized recursive solution to Fibonacci sequence
    
    :param n: the nth number in the Fibonacci sequence
    :return: the value of the nth number in the Fibonacci sequence
    """
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


@lru_cache(maxsize=None)
def fib_lru(n: int) -> int:
    """Memoized recursive solution using functools LRU cache

    :param n: the nth number in the Fibonacci sequence
    :return: the value of the nth number in the Fibonacci sequence
    """
    if n < 2:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


def fib_iter(n: int) -> int:
    """Iterative solution
    
    :param n: the nth number in the Fibonacci sequence
    :return: the value of the nth number in the Fibonacci sequence
    """
    if n == 0:
        return 0
    last, next = 0, 1
    for _ in range(1, n):
        last, next = next, last + next
    return next
    


def fib(n):
    return fib_iter(n)


def main():
    print(fib(50))


if __name__ == "__main__":
    main()
