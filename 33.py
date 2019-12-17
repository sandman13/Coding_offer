# -*- coding:utf-8 -*-


#将数组排成最小的数


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        numstr = map(str,numbers) #用str方式将int型数字转换成string
        l = lambda n1,n2:int(n1+n2)-int(n2+n1)# 指定比较方式
        numsort = sorted(numstr,cmp=l) #用特定的比较方式进行比较
        return "".join(i for i in numsort) #拍完序之后用join进行连接成结果



if __name__=='__main__':
    s=Solution()
    numbers=[3,32,321]
    print(s.PrintMinNumber(numbers))