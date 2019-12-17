# -*- coding:utf-8 -*-


#连续子数组的最大和

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if array==None or len(array)==0:
            return 0

        curSum=0   #当前的和
        maxSum=-1000
        for i in range(0,len(array)):
            if curSum<=0:
                curSum=array[i]   #前面的总和是一个负数的话，此时将重置子数组为当前数
            else:
                curSum+=array[i]

            if curSum>maxSum:
                maxSum=curSum

        return maxSum


    def find2(self,array):
        #使用动态规划法，f(i)表示以第i个数字结尾的子数组的最大和
        result=[0]*len(array)
        result[0]=array[0]
        maxsum=-1000

        for i in range(1,len(array)):
            if result[i-1]<=0:
                result[i]=array[i]
            else:
                result[i]=array[i]+result[i-1]

        return max(result),result



if __name__=='__main__':
    s=Solution()
    array=[1,-2,3,10,-4,7,2,-5]
    print(s.FindGreatestSumOfSubArray(array))
    print(s.find2(array))