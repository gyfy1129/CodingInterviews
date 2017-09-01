def rectangle(n):
    one = 1
    two = 2
    if n == 1:
        num = 1
    elif n == 2:
        num = 2
    elif n > 2:
        for i in range(3, n+1):
            num = one + two
            one = two
            two = num
    return num

if __name__ == "__main__":
    print rectangle(5)


