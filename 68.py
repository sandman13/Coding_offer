# -*- coding:utf-8 -*-

#剪绳子

#给你一根长度为n的绳子，请把绳子剪成整数长的m段（m、n都是整数，n>1并且m>1），每段绳子的长度记为k[0],k[1],...,k[m]。
# 请问k[0]xk[1]x...xk[m]可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

#动态规划法：f(n)=f(i)*f(n-i)

class Solution:
    def cutRope(self, number):
        # write code here
        #由于要满足n>1,m>1的条件
        if (number < 2):
            return 0
        if (number == 2):
            return 1
        if (number == 3):
            return 2

        result=[0,1,2,3]
        for i in range(4,number+1):
            max=0
            for j in range (1,i//2+1):
                temp=result[j]*result[i-j]
                if temp>max:
                    max=temp
            result.append(max)
        return result[number]

if __name__=='__main__':
    s=Solution()
    print(s.cutRope(8))
