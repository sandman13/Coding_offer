#-*- coding:utf-8 -*-

#反转链表：需要定义三个指针
#（1）指向自身的指针
#（2）指向前一个节点的指针：因为需要修改指针指向
#（3）指向后一个节点的指针：防止出现断链现象

#需要考虑的情况：输入的链表表头指针为NULL，输入的链表只有一个节点，输入的链表有多个节点


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pNode=pHead
        pNodePre=None
        pResult=None
        while pNode:
            pNodeNext=pNode.next
            if pNodeNext==None:
                pResult=pNode

            pNode.next=pNodePre

            pNodePre=pNode
            pNode=pNodeNext

        return pResult
