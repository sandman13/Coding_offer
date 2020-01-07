# -*- coding:utf-8 -*-

#删除排序链表中重复的节点

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

     def printList(self):
         while self!=None:
             print(self.val)
             self=self.next


class Solution:
    #从头开始创建一个新的链表
    def deleteDuplication(self, pHead):
        # write code here
        # 创建临时节点，并将链表连接在临时节点上
        d = ListNode(-1)
        d.next = pHead

        pre = d
        cur = pHead

        while cur:
            if cur.next and cur.next.val == cur.val:
                tmp = cur.next
                while tmp and tmp.val == cur.val:
                    tmp = tmp.next

                # 当上一行循环退出后代表找到第一个与cur所指向的节点值不同的节点
                pre.next = tmp
                cur = tmp
            else:
                pre = cur
                cur = pre.next

        return d.next



if __name__=="__main__":
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(2)
    node4=ListNode(3)
    node1.next=node2
    node2.next=node3
    node3.next=node4
    s=Solution()
    node=s.deleteDuplication(node1)
    node.printList()

