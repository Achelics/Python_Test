#!/usr/bin/env/ python
# coding=utf-8

"""
    ID: mutil_process_test.py
    Subject: Description the mutil process handler.
"""
__author__ = 'Achelcis'
__Date__ = '2016/12/15'

from multiprocessing import Pool
from time import sleep

def f(x):
    for i in range(10):
        print '%s ------ %s ' %(i, x)
        sleep(1)

def main():
    result = None
    pool = Pool(processes=3)  # set the processes max number 3
    for i in range(11, 20):
        result = pool.apply_async(f, (i,))

    pool.close()
    pool.join()
    if result.successful():
        print "successful"


if __name__ == '__main__':
    main()
