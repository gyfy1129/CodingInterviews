#coding=utf-8
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        root = TreeNode(pre[0])

        mid = tin.index(pre[0])
        tin_left = tin[0:mid]
        tin_right = tin[mid + 1:len(tin)]

        pre_left = pre[1:len(tin_left)+1]
        pre_right = pre[len(tin_left)+1:len(pre)]

        if len(pre_left) != 0 and len(tin_left) != 0:
            root.left = self.reConstructBinaryTree(pre_left,tin_left)
        if len(pre_right) != 0 and len(tin_right) != 0:
            root.right = self.reConstructBinaryTree(pre_right,tin_right)

        return root


if __name__=="__main__":
    bat = Solution()
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    tree = bat.reConstructBinaryTree(pre,tin)
    print tree
