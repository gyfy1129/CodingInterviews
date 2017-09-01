def numberof1(n):
    flag = 1
    count = 0
    for i in range(32):
        if n&flag:
            count = count + 1
        flag = flag << 1

    return count


def numberof1_1(n):
    count = 0
    for i in range(32):
        if (n>>i)&1:
            count = count +1
    return count



if __name__ == "__main__":
    print numberof1(9)