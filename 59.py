# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#对称的二叉树

class Solution:
    def isSymmetrical(self, pRoot):
        return self.check(pRoot,pRoot)


    def check(self,Root1,Root2):
        if Root1==None and Root2==None:
            return True
        if Root1==None or Root2==None:
            return False

        if Root1.val!=Root2.val:
            return False

        return self.check(Root1.left,Root2.right) and self.check(Root1.right,Root2.left)