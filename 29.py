#-*- coding:utf-8 -*-

#数组中出现次数超过一半的数字


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        dict={}
        for num in numbers:
            dict[num]=1 if num not in dict else dict[num]+1
            if dict[num]*2>len(numbers):
                return num
        return 0