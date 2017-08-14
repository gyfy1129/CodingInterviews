#coding=utf-8
def frog(n):  # 青蛙跳递归法
    if n == 0:
        sum = 0
    elif n == 1:
        sum = 1
    elif n == 2:
        sum = 2
    elif n > 2:
        sum = frog(n - 1) + frog(n - 2)
    return sum

# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, n):
        if n == 0:
            num = 0
        elif n == 1:
            num = 1
        elif n == 2:
            num = 2
        elif n > 2:
            one = 1
            two = 2
            for i in range(3, n + 1):
                num = one + two
                one = two
                two = num

        return num
def frog1(n):  # 青蛙跳非递归法
    if n == 0:
        num = 0
    elif n == 1:
        num = 1
    elif n == 2:
        num = 2
    elif n > 2:
        one = 1
        two = 2
        for i in range(3,n+1):
            num = one + two
            one = two
            two = num

    return num

if __name__ == "__main__":
    print frog1(100)
