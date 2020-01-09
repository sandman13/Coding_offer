# -*- coding:utf-8 -*-


#滑动窗口中的最大值


class Solution:
    def maxInWindows(self, num, size):
        # write code here
        # 存放可能是最大值的下标
        maxqueue = []
        # 存放窗口中最大值
        maxlist = []
        n = len(num)
        # 参数检验
        if n == 0 or size == 0 or size > n:
            return maxlist
        for i in range(n):
            # 判断队首下标对应的元素是否已经滑出窗口
            if len(maxqueue) > 0 and i - size >= maxqueue[0]:
                maxqueue.pop(0)
            while len(maxqueue) > 0 and num[i] > num[maxqueue[-1]]:
                maxqueue.pop()
            maxqueue.append(i)
            if i >= size - 1:
                maxlist.append(num[maxqueue[0]])
        return maxlist

    def max2(self,num,size):
        '''
        简单的做法
        :param num:
        :param size:
        :return:
        '''
        i = 0
        leng = len(num)
        ret = []
        while i < leng - size + 1:
            ret.append(max(num[i:i + size]))
            i += 1
        return ret

if __name__=='__main__':
    num=[2,3,4,2,6,2,5,1]
    s=Solution()
    print(s.max2(num,3))