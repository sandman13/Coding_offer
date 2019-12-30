# -*- coding:utf-8 -*-


#圆圈中最后剩下的数字

#创新解法，得到递推公式：f(n,m)=[f(n-1,m)+m]%n n>1;f(n,m)=0 n=1

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n<1 or m<1:
            return -1
        last=0
        for i in range(2,n+1):
            last=(last+m)%i
        return last

    def Sum_Solution(self, n):
        #求和运算，不可以使用循环等别的操作，这里使用逻辑与的短路特性来使得递归终止
        result=n
        temp=n>0 and self.Sum_Solution(n-1)
        result=result+temp
        return result

    def Add(self, num1, num2):
        #两数之和：不用四则运算，只能使用位运算来代替
        while num2:
            result = (num1 ^ num2) & 0xffffffff
            carry = ((num1 & num2) << 1) & 0xffffffff
            num1 = result
            num2 = carry
        if num1 <= 0x7fffffff:
            result = num1
        else:
            result = ~(num1 ^ 0xffffffff)
        return result

if __name__=='__main__':
    str=input()
    n,m=str[0],str[1]
    s=Solution()
    print(s.LastRemaining_Solution(n,m))