# -*- coding:utf-8 -*-


#最小的k个数

class Solution:

    def GetLeastNumbers_Solution(self, tinput, k):
        n = len(tinput)
        if k <= 0 or k > n:
            return list()
        start = 0
        end = n - 1
        mid = self.partition(tinput, start, end)
        while k - 1 != mid:
            if k - 1 > mid:
                start = mid + 1
                mid = self.partition(tinput, start, end)
            elif k - 1 < mid:
                end = mid - 1
                mid = self.partition(tinput, start, end)
        res = tinput[:mid + 1]
        # res.sort()
        return res


    def partition(self, numbers, low, high):
        key = numbers[low]
        while low < high:
            while low < high and numbers[high] >= key:
                high -= 1
            numbers[low] = numbers[high]
            while low < high and numbers[low] <= key:
                low += 1
            numbers[high] = numbers[low]
        numbers[low] = key
        return low


if __name__=='__main__':
    numbers=[4,5,1,6,2,7,3,8]
    s=Solution()
    print(s.GetLeastNumbers_Solution(numbers,4))