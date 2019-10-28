"""
c1_fibonacci
Created October 28, 2019 by Jennifer Baughman

Description:
"""

memo = {1: 0, 2: 1}


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


def fib(n):
    return fib_recurs(n)


def main():
    print(fib(5))


if __name__ == "__main__":
    main()
