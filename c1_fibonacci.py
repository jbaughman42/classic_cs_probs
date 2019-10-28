"""
c1_fibonacci
Created October 28, 2019 by Jennifer Baughman

Description:
"""


def fib_recurs(n: int) -> int:
    """Basic recursive solution to Fibonacci sequence
    
    :param n: the nth number in the Fibonacci sequence
    :return: the value of the nth number in the Fibonacci sequence
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib_recurs(n-1) + fib_recurs(n-2)
    


def fib(n):
    return fib_recurs(n)


def main():
    print(fib(5))


if __name__ == "__main__":
    main()
