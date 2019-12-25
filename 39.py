# -*- coding:utf-8 -*-

#求解二叉树的深度
#判断一棵树是否是平衡二叉树


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0
        return max(self.TreeDepth(pRoot.left),self.TreeDepth(pRoot.right))+1

    def IsBalanced_Solution(self, pRoot):
        '''
        使用递归来判断是否是二叉平衡树,重复遍历会影响性能
        :param pRoot:
        :return:
        '''
        if pRoot is None:
            return True
        left=self.TreeDepth(pRoot.left)
        right=self.TreeDepth(pRoot.right)
        diff=abs(left-right)
        if diff>1:
            return False

        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)



if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node1.left=node2
    node2.left=node3
    s=Solution()
    print(s.IsBalanced_Solution(node1))