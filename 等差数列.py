import sys
def f2(s):
    length = len(s)
    s.sort()
    s = map(int, s)
    for i in range(1,length-2):
        if s[i+1] - s[i] == s[i] - s[i-1]:
            continue
        else:
            return 'impossible'
    return 'possible'


if __name__ =="__main__":
    #list = raw_input()
    #list = "1 3 2 4 6 5 "
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    print f2(line.split())

