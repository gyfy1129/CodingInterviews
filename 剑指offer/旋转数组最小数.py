#coding=utf-8
def sort(ary):  # 旋转数组最小数
    n = len(ary)
    left = 0
    right = n-1
    if n == 0:
        return 0
    if n == 1:
        return ary[0]

    while left<=right:
        if right-left<=1:
            return ary[right]


        mid = (left + right)/2

        if ary[left]==ary[right]==ary[mid]:
            return Mid(ary,left,right)

        if ary[mid]>=ary[left]:
            left = mid
        elif ary[mid]<=ary[right]:
            right = mid

    return ary[right]


def Mid(ary, left, right):
    n = len(ary)
    left = 0
    temp = left
    right = n - 1
    for i in range(1, n - 1):
        if ary[temp] > ary[i]:
            ary[temp] = ary[i]
    return ary[temp]


num = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
print sort(num)





