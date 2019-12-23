#-*- coding:utf-8 -*-


#逆序对：利用归并排序求解逆序对O(nlogn)  注：用python这两种做法都没有100%AC

class Solution:
    def InversePairs(self, data):
        # write code here
        global cnt
        cnt = 0
        p = self.guibing(data)
        return cnt%1000000007
    def guibing(self,data):
        global cnt
        if len(data) == 1:
            return data
        mid = len(data)//2
        left = self.guibing(data[:mid])
        right = self.guibing(data[mid:])
        i = 0
        j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                cnt += len(left) - i  #计算逆序对的数量
                j += 1
        res += left[i:]
        res += right[j:]
        return res

    def InversePairs2(self, data):
        #直接对复制的数组进行排序，然后每一选择最小的数看它在原数组中的位置，前面的都是逆序，每做一次操作都在原数组中删除这个数
        # write code here
        cnt = 0
        copy = data[:]
        copy.sort()
        for i in copy:
            cnt += data.index(i)
            data.remove(i)
        return cnt % 1000000007

if __name__=='__main__':
    data=[7,5,6,4]
    s=Solution()
    print(s.InversePairs(data))