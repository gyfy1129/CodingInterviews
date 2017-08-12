def f1():
    s = raw_input()
    length = len(s)
    l = []
    n = 1

    if length == 0:
        return 0
    if length == 1:
        return 1
    if length > 1:
        for i in range(0, length - 1):
            if s[i] is not s[i + 1]:
                n = n + 1
                l.append(n)
                continue
            elif s[i] is s[i + 1]:
                n = 1
            l.append(n)

    num = len(l)
    for m in range(0,num-1):
        if l[m] > l[m+1]:
            l[m],l[m+1] = l[m+1],l[m]
        elif l[m] > l[m+1]:
            m = m + 1

    return l[num-1]


if __name__ == "__main__":
    print f1()
