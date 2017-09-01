#coding=utf-8
# 行：row 列：col
class Solution:
    # array 二维列表
    def Find(self, n,matrix):
        maxrow = len(matrix)
        if maxrow == 0:
            return False
        maxcol = len(matrix[0])
        if n == '':
            return False
        # for i in range(0,maxrow):
        j = maxcol-1
        i = 0
        while j >= 0 and i < maxrow:
            if matrix[i][j] > n:
                j = j - 1
            elif matrix[i][j] < n:
                i = i + 1
            elif matrix[i][j] == n:
                return True
        return False


if __name__=='__main__':
    ba = Solution()
    num = [[1,2,3],[2,3,4],[3,4,5]]
    num1 = [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
    n = 16
    print ba.Find(n,num1)
    # if find(num,n) is True:
    #     print 'get'
    # elif find(num,n) is False:
    #     print 'null'