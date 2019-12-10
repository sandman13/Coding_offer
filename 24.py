#-*- coding:utf-8 -*-

#判断一组数字是不是二叉搜索树的后序遍历结果
#后序遍历最后一个数字是根节点，那么前面的数字可以划分为两个部分：前面一部分小于根节点，后面大于根节点


class Solution:
    def VerifySquenceOfBST(self, sequence):
        if len(sequence)==0:
            return False
        length=len(sequence)
        root=sequence[length-1]

        #在二叉搜索树中左子树的节点小于根节点
        i=0
        while i<length-1:
            if sequence[i]>root:
                break
            i+=1

        j=i
        while j<length-1:
            if sequence[j]<root:
                return False
            j+=1

        #递归判断左子树是否是二叉搜索树
        left=True
        if i>0:
            left=self.VerifySquenceOfBST(sequence[0:i])
        right=True
        if i<length-1:
            right=self.VerifySquenceOfBST(sequence[i:length-1])

        return left and right


if __name__=='__main__':
    sequence=[7,4,6,5]
    s=Solution()
    print(s.VerifySquenceOfBST(sequence))