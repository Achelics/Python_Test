#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelcis'
__Date__ = '2016/10/08'


def fib(n):
    """ Generator for Fibonacci serie
    Example: for i in fib(5): print i
    :param n: fib range upper bound
    :return:
    """
    if not n:
        return
    a, b = 0, 1
    yield a
    i = 0
    while i < n-1:
        yield b
        a, b = b, a+b
        i += 1


if __name__ == '__main__':
    f = fib(5)
    for i in f:
        print i
