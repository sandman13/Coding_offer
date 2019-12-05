#-*- coding:utf-8 -*-

#合并两个有序的链表

#需要对空链表单独处理
#递归的过程

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1==None:
            return pHead2
        elif pHead2==None:
            return pHead1

        pResult=None

        if pHead1.val<pHead2.val:
            pResult=pHead1
            pResult.next=self.Merge(pHead1.next,pHead2)

        else:
            pResult=pHead2
            pResult.next=self.Merge(pHead1,pHead2.next)

        return pResult