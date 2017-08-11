#coding=utf-8
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1)+fib(n-2)

print fib(10)

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        fibone = 1
        fibtwo = 1
        fibn = 0
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(2, n):
            fibn = fibone + fibtwo
            fibone = fibtwo
            fibtwo = fibn

        return fibn
bc = Solution()
print bc.Fibonacci(100)


def fib2(n):
    fibone = 0
    fibtwo = 1
    fibn = 0
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        for i in range(2, n+1):
            fibn = fibone + fibtwo
            fibone = fibtwo
            fibtwo = fibn

    return fibn

print fib2(2)