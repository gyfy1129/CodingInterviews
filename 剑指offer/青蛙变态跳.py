def maxfrog(n):
    first = 1
    second = 2
    if n == 0:
        num = 0
    elif n == 1:
        num = 1
    elif n > 1:
        num = 2**(n-1)
    return num
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        first = 1
        second = 2
        if number == 0:
            num = 0
        elif number == 1:
            num = 1
        elif number > 1:
            num = 2 ** (number - 1)
        return num

if __name__ == "__main__":
    print maxfrog(5)
