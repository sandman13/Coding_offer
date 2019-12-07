#-*- coding:utf-8 -*-
#实现一个min()函数的栈
#思想就是利用一个辅助栈来存储所有当过最小值的元素，
# 注意在pop的时候如何pop的值和当前最小栈的栈顶元素相等，则两个都要pop

class Solution:
    def __init__(self):
        self.q = []

    def push(self, node):
        # write code here
        curMin = self.min()
        if curMin == None or node < curMin:
            curMin = node
        self.q.append((node, curMin))

    def pop(self):
        # write code here
        if len(self.q) == 0:
            return None
        else:
            return self.q.pop()

    def top(self):
        # write code here
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][0]

    def min(self):
        # write code here
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]


if __name__=='__main__':
    s=Solution()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(1)
    print(s.q)