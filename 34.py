# -*- coding:utf-8 -*-


#丑数：只能被2，3，5整除的数

class Solution:
    def GetUglyNumber_Solution(self, index):

        if index==0:
            return 0
        uglyList=[1]
        index2=index3=index5=0
        cursum=1
        while(cursum<index):
            minNum=min(uglyList[index2]*2,uglyList[index3]*3,uglyList[index5]*5)
            uglyList.append(minNum)
            while uglyList[index2]*2<=minNum:
                index2+=1

            while uglyList[index3]*3<=minNum:
                index3+=1

            while uglyList[index5]*5<=minNum:
                index5+=1

            cursum+=1
        return uglyList[-1]


if __name__=='__main__':
    s=Solution()
    print(s.GetUglyNumber_Solution(5))