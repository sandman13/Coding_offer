#-*- coding:utf-8 -*-

#从上往下打印二叉树,广度遍历

class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        #利用队列来实现
        q=[]
        result=[]  #存放结果数据
        if root==None:
            return result
        q.append(root)
        while len(q)!=0:
            tmp=q[0]
            q.pop(0)
            result.append(tmp.val)
            if tmp.left!=None:
                q.append(tmp.left)
            if tmp.right!=None:
                q.append(tmp.right)
        return result


if __name__=="__main__":
    t1=TreeNode(1)
    t2=TreeNode(2)
    t3=TreeNode(3)
    t4=TreeNode(4)
    t1.left=t2
    t1.right=t3
    t2.left=t4
    s=Solution()
    print(s.PrintFromTopToBottom(t1))