# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#按照层次遍历打印二叉树

class Solution:
    def Print(self, pRoot):
        ans = []
        if not pRoot:
            return ans
        queue = []
        queue.append(pRoot)
        while queue:
            cnt = 0
            size = len(queue)
            row = []
            while cnt < size:
                node = queue.pop(0)
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cnt += 1
            ans.append(row)
        return ans

    def Print2(self, pRoot):
        '''
        之字形打印二叉树
        :param pRoot:
        :return:
        '''
        ans = []
        if not pRoot:
            return ans
        queue = []
        queue.append(pRoot)
        flag=True
        while queue:
            cnt = 0
            size = len(queue)
            row = []
            while cnt < size:
                node = queue.pop(0)
                row.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cnt += 1
            if flag:
                ans.append(row)
            else:
                ans.append(list(reversed(row)))
            flag=not flag
        return ans
