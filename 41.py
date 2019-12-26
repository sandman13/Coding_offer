# -*- coding:utf-8 -*-


#输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。


class Solution:
    def FindNumbersWithSum(self, array,tsum):
        #从前和从后同时向中间找
        if array is None or len(array)==0:
            return []
        result=[]
        left=0
        right=len(array)-1
        while left<right:
            if array[left]+array[right]==tsum:
                result.append([array[left],array[right]])
                left+=1
                right-=1
            elif array[left]+array[right]>tsum:
                right-=1
            else:
                left+=1
        min=10000000
        min_index=0
        if len(result)==0:
            return result
        for temp in result:
            if temp[0]*temp[1]<min:
                min=temp[0]*temp[1]
                min_index=result.index(temp)
        return result[min_index]

    def FindContinuousSequence(self,tsum):
        '''
        采用上一题一样的思想，类似于滑动窗口，两个指针，指向序列的范围
        :param array:
        :param tsum:
        :return:
        '''
        if tsum<3:
            return []
        result=[]
        small=1
        big=2
        middle=(1+tsum)/2
        curSum=small+big
        while small<middle:
            if curSum==tsum:
                temp=[]
                for i in range(small,big+1):
                    temp.append(i)
                result.append(temp)
            while curSum>tsum and small<middle:
                curSum-=small
                small+=1
                if curSum==tsum:
                    temp = []
                    for i in range(small, big + 1):
                        temp.append(i)
                    result.append(temp)
            big+=1
            curSum+=big
        return result





if __name__=='__main__':
    array=[1,2,4,7,11,15]
    s=Solution()
    print(s.FindContinuousSequence(15))