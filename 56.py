# -*- coding:utf-8 -*-

#链表中环的入口节点
#使用快慢指针，让第一个指针向前先走n步（n表示环中节点的数目），然后二者同时走，相遇时的节点就是入口节点

#如何计算环中节点的个数：也是使用一快一慢指针，二者相遇的节点一定在环中，那么从这个节点出发开始计数，再次到达这个节点的时候就是节点的个数

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution:
    def EntryNodeOfLoop(self, pHead):
        meetingNode=self.getLoopNum(pHead)
        if meetingNode==None:
            return None
        #获取环中的节点
        num=1
        pNode=meetingNode
        while pNode.next !=meetingNode:
            pNode=pNode.next
            num+=1
        #移动快指针
        pNode1=pHead
        for i in range(0,num):
            pNode1=pNode1.next

        #两个指针同时移动
        pNode2=pHead
        while pNode1!=pNode2:
            pNode1=pNode1.next
            pNode2=pNode2.next

        return pNode1




    def getLoopNum(self,pHead):
        if pHead is None:
            return None
        pSlow=pHead.next
        if pSlow is None:
            return None
        pFast=pSlow.next
        while pSlow !=None and pFast!=None:
            if pFast==pSlow:
                return pFast
            pSlow=pSlow.next
            pFast=pFast.next
            if pFast!=None:
                pFast=pFast.next
        return None
