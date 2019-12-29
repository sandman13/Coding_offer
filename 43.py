# -*- coding:utf-8 -*-

#扑克牌的顺子

#从扑克牌中随机抽取5张牌，大小王可以变为任意一张牌，判断这种规则下能否变成一个顺子

class Solution:
    def IsContinuous(self, numbers):
        '''
        先将数组排序，大小王使用0代替，找到数组中0的个数，以及相邻两个数之间的间隔的总和
        :param numbers:
        :return:
        '''
        if numbers is None or len(numbers)==0:
            return False
        numbers=sorted(numbers)
        print(numbers)
        numZero=0
        numGap=0
        for num in numbers:
            if num==0:
                numZero+=1

        #间隔总和
        for i in range(numZero+1,len(numbers)):    #注意这里计算间隔的时候，不应该考虑0和别的元素之间的间隔，起始位置应该从第一个不为0的数开始
            if numbers[i]==numbers[i-1]:
                #有对子
                return False
            numGap+=numbers[i]-numbers[i-1]-1

        if numGap>numZero:
            return False
        else:
            return True


if __name__=='__main__':
    numbers=[1,0,0,3,5]
    s=Solution()
    print(s.IsContinuous(numbers))