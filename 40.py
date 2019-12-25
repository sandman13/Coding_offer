# -*- coding:utf-8 -*-


#一个整型数组里除了两个数字之外，其他的数字都出现了两次，找出这两个只出现了一次的数字
#时间复杂度o(n),空间复杂度o(1)


#如果数组里只有一个只出现一次的数字，那么这个时候可以使用异或的思想，从头到尾一次异或，最后剩下的就是只出现一次的数字

#这里有两个数字，可以考虑划分为两个子数组，即每一部分包含一个只出现一次的数

'''
以{2,4,3,6,3,2,5,5}为例：

我们依次对数组中的每个数字做异或运行之后，得到的结果用二进制表示是0010。
异或得到结果中的倒数第二位是1，于是我们根据数字的倒数第二位是不是1分为两个子数组。
第一个子数组{2,3,6,3,2}中所有数字的倒数第二位都是1，而第二个子数组{4,5,5}中所有数字的倒数第二位都是0。
接下来只要分别两个子数组求异或，就能找到第一个子数组中只出现一次的数字是6，而第二个子数组中只出现一次的数字是4。
'''


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array is None or len(array)<2:
            return None
        remain,index=0,1
        for num in array:
            remain=remain^num
        while(remain&index)==0:
            index=index<<1
        res1,res2=0,0
        for num in array:
            if num&index==0:
                res1=res1^num
            else:
                res2=res2^num
        return [res1,res2]

if __name__=='__main__':
    array=[2,3,2,3,4,6]
    s=Solution()
    print(s.FindNumsAppearOnce(array))
