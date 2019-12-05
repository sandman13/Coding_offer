#-*- coding:utf-8 -*-

#输入两棵二叉树A和B，判断B是不是A的子结构

'''
两个函数：
（1）在A中遍历寻找是否有B的根节点的值，本质是二叉树的遍历，可以使用递归
（2）在A中找到节点之后，需要判断以这个节点为根的子树是否包含B，又是一次递归
'''

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result=False
        if pRoot1 and pRoot2:
            if pRoot1.val==pRoot2.val:
                result=self.DoesTree1HasTree2(pRoot1,pRoot2)

            if result==False:
                result=self.HasSubtree(pRoot1.left,pRoot2)

            if result==False:
                result=self.HasSubtree(pRoot1.right,pRoot2)
        return result


    def DoesTree1HasTree2(self,pRoot1,pRoot2):
        if pRoot2==None:
            return True
        if pRoot1==None:
            return False

        if pRoot1.val != pRoot2.val:
            return False

        return self.DoesTree1HasTree2(pRoot1.left,pRoot2.left) and self.DoesTree1HasTree2(pRoot1.right,pRoot2.right)