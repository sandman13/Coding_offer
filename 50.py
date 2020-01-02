# -*- coding:utf-8 -*-


#在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。
# 也不知道每个数字重复几次。请找出数组中任意一个重复的数字

#使用一个空间复杂度为o(1)的算法

class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        if numbers is None or len(numbers)==0:
            return False
        for i in range(0,len(numbers)):
            #如果当前这个数正好等于这个下标，则说明是在正确的位置
            while numbers[i]!=i:
                if numbers[i]==numbers[numbers[i]]:
                    #如果这个数值为m,下标为m的位置上的值如果和m不相等秒，那么就调换位置
                    duplication.append(numbers[i])
                    return True
                else:
                    temp=numbers[i]
                    numbers[i]=numbers[temp]
                    numbers[temp]=temp
        return False

if __name__=='__main__':
    s=Solution()
    numbers=[2,3,1,0,2,5,3]
    dup=[]
    print(s.duplicate(numbers,dup))
