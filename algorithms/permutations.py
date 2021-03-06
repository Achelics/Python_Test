#!/usr/bin/env/ python
# coding=utf-8
__author__ = 'Achelics'
__Date__ = '2016/10/08'


def permutations(l):
    """Generator for list permutations.

    :param l: list to generate permutations for
    :return: yield each permutations
    Example:
    l = [1, 2, 3]
    a = [1]
    permutations([2, 3]) = [[2,3], [3,2]]
    [2,3]
    yield [1,2,3]
    yield [2,1,3]
    yield [2,3,1]
    [3,2]
    yield [1,3,2]
    yield [3,1,2]
    yield [3,2,1]
    """
    if len(l) <= 1:
        yield l
    else:
        a = [l.pop(0)]
        for p in permutations(l):
            for i in range(len(p) + 1):
                yield p[:i] + a + p[i:]

if __name__ == '__main__':
    l = [2, 3, 4]
    for list in permutations(l):
        print list
