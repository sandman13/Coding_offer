# -*- coding:utf-8 -*-

#求两个链表的第一个公共结点

#首先遍历两个链表，得到链表的长度，让长的链表先走，然后再同时在两个链表上遍历，找到的第一个相同的结点就是第一个公共结点
#o(m+n)
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

     def printNode(self):
         pNode=self
         while pNode is not None:
             print(pNode.val)
             pNode=pNode.next


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 ==None or pHead2==None:
            return None
        #获取两个链表的长度
        len1=self.getLength(pHead1)
        len2=self.getLength(pHead2)
        len=abs(len1-len2)
        if len1>len2:
            pheadLong=pHead1
            pheadShort=pHead2
        else:
            pheadLong=pHead2
            pheadShort=pHead1

        i=0
        while i<len and pheadLong is not None:
            pheadLong=pheadLong.next

        while pheadLong is not None and pheadShort is not None and pheadLong!=pheadShort:
            pheadLong=pheadLong.next
            pheadShort=pheadShort.next

        return pheadLong


    def getLength(self,pHead):
        length=0
        pNode=pHead
        while pNode is not None:
            length+=1
            pNode=pNode.next
        return length

    def FindFirstCommonNode2(self, pHead1, pHead2):
        '''
        将两个链表拼接，一个是p1在前p2在后，另一个是p2在前p1在后，得到两个长度相同的链表，遍历找第一个公共结点
        :param pHead1:
        :param pHead2:
        :return:
        '''
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        cur1, cur2 = pHead1, pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 != None else pHead2
            cur2 = cur2.next if cur2 != None else pHead1
        return cur1

if __name__=='__main__':
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(3)
    node4=ListNode(4)
    node5=ListNode(5)
    node1.next=node3
    node2.next=node4
    node3.next=node5
    node4.next=node5
    s=Solution()
    common=s.FindFirstCommonNode(node1,node2)
    common.printNode()
