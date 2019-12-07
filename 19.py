#-*- coding:utf-8 -*-


#给定二叉树，求其镜像


class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        #当是空树
        if root==None:
            return root
        #递归
        self.Mirror(root.left)
        self.Mirror(root.right)
        root.left,root.right=root.right,root.left
