#-*- coding:utf-8 -*-

#二叉树中和为某一值的所有路径
#路径：从根节点到叶子结点

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        list=[]
        if not root:
            return list

        if not root.left and not root.right and root.val==expectNumber:
            return [[root.val]]

        else:
            #如果不是叶子节点，则递归计算它的子树
            left=self.FindPath(root.left,expectNumber-root.val)
            right=self.FindPath(root.right,expectNumber-root.val)

            for item in left+right:
                list.append([root.val]+item)
        return list

if __name__=='__main__':
    t1=TreeNode(10)
    t2=TreeNode(5)
    t3=TreeNode(12)
    t4=TreeNode(4)
    t5=TreeNode(7)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    t2.right=t5
    s=Solution()
    print(s.FindPath(t1,22))