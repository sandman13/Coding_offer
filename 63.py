# -*- coding:utf-8 -*-
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#二叉搜索树的第k个节点

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        # 中序遍历二叉树
        if not pRoot or k <= 0:
            return None
        node_stack = []
        node = pRoot
        while node or node_stack:
            while node:
                node_stack.append(node)
                node = node.left
            node = node_stack.pop()
            k -= 1
            if k == 0:
                return node
            node = node.right
        if k > 0:
            return None


if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    node1.left=node2
    node1.right=node3
    node2.right=node4
    node3.left=node5
    s=Solution()
    result=s.KthNode(node1,1)
    print(result.val)