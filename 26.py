#-*- coding:utf-8 -*-

#复杂链表的复制 :(1)首先将复制的链表间隔插在原始链表的后面：A-A'-B-B'...
#(2)如果A有随机链表指向的话，复制的节点的随机链表指向就应该是后一个节点
#（3）将链表按照奇偶位置分割为两个部分

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

    def print_list(self,pHead):  # 遍历链表，并将元素依次打印出来
        print("linked_list:")
        temp =pHead # 临时变量指向队列头部
        while temp is not None:
            print(temp.label)
            temp = temp.next


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        pHead=self.cloneNodes(pHead)
        pHead=self.connectRandom(pHead)
        return self.Reconnect(pHead)

    def cloneNodes(self,pHead):
        pNode=pHead
        while pNode:
            pCloned=RandomListNode(pNode.label)
            pCloned.next=pNode.next
            pNode.next=pCloned
            pNode=pCloned.next
        return pHead

    def connectRandom(self,pHead):
        pNode=pHead
        while pNode:
            pCloned=pNode.next

            if pNode.random:
                pCloned.random=pNode.random.next
            pNode=pCloned.next
        return pHead

    def Reconnect(self,pHead):
        pNode=pHead
        pClonedHead=None
        pClonedNode=None

        #头节点需要单独处理
        if pNode:
            pClonedHead=pClonedNode=pNode.next
            pNode.next=pClonedNode.next
            pNode=pNode.next

        while pNode:
            pClonedNode.next=pNode.next
            pClonedNode=pClonedNode.next
            pNode.next=pClonedNode.next
            pNode=pNode.next
        return pClonedHead

if __name__=='__main__':
    t1=RandomListNode('A')
    t2=RandomListNode('B')
    t3=RandomListNode('C')
    t1.next=t2
    t1.random=t3
    t2.next=t3

    s=Solution()
    pClone=s.Clone(t1)
    pClone.print_list(pClone)
