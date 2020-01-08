# -*- coding:utf-8 -*-

#二叉树的下一个节点：找到中序遍历顺序下的下一个节点

class TreeLinkNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         self.next = None  #指向父节点


class Solution:
    def GetNext(self, pNode):
        '''
        1.如果一个节点有右子树，那么下一个节点就是它的右子树的最左节点
        2.如果没有右子树，并且这个节点是父节点的左子树，那么下一个节点就是这个节点的父节点
        3.如果是没有右子树，并且是父节点的右子树的节点，沿着父节点的指针一直向上找，知道找到某个节点是父节点的左子树，这时下一个节点就是这个父节点

        :param pNode:
        :return:
        '''
        if pNode == None:
            return None
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        p = pNode.next
        if p and p.left == pNode:
            return p
        else:
            while (p and p.left != pNode):
                pNode = p
                p = p.next
            return p

