#-*- coding:utf-8 -*-

#链表中倒数第k个节点，要注意代码的鲁棒性，考虑一些边界情况


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head==None or k<=0:
            return None
        p1=head
        p2=None
        for i in range(0,k-1):
            if p1.next!=None:
                p1=p1.next
            else:
                return None

        p2=head
        while p1.next!=None:
            p1=p1.next
            p2=p2.next
        return p2


if __name__=='__main__':
    node1=ListNode(1)
    node2=ListNode(2)
    node3=ListNode(3)
    node1.next=node2
    node2.next=node3
    node3.next=None

    s=Solution()
    print(s.FindKthToTail(node1,1).val)


