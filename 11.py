#-*- coding:utf-8 -*-


#实现函数double power(base,exponent),不使用库函数，也不需要考虑大数问题

#这道题的考点在于注意细节：（1）base为0的时候，指数为负怎么办；（2）指数为负和指数为0的情况
# (3)float,double类型的小数在比较的时候不能直接用=号比较，而应该是两者的差的绝对值小于某个数就认为相等

class Solution:

    def equal(self,num1,num2):
        '''
        判断两个小数是否相等
        :param num1:
        :param num2:
        :return:
        '''
        if num1-num2>-0.0000001 and num1-num2<0.0000001:
            return True
        else:
            return False

    #全面但是不高效
    def Power(self,base, exponent):

        #当底数为0，指数小于0时，直接返回底数
        if self.equal(base,0.0) and exponent<0:
            return 0.0

        #取指数的绝对值
        if exponent>0:
            absExponent=exponent
        else:
            absExponent=-exponent

        '''
        result=1.0
        for i in range(1,absExponent+1):
            result*=base
        '''
        result=self.powerWithUnsigned(base,absExponent)

        if exponent<0:
            return 1.0/result
        return result

    #全面又高效的算法
    def powerWithUnsigned(self,base,exponent):
        #上一种做法会做exponent次乘法，但是这一部分可以换成可以通过递归来求解，o(logn)
        if exponent==0:
            return 1
        if exponent==1:
            return base
        result=self.powerWithUnsigned(base,exponent>>1)   #使用右移取代除法
        result*=result
        if(exponent & 0x1==1):
            #判断指数是否是奇数
            result*=base

        return result



if __name__=='__main__':
    s=Solution()
    print(Solution.Power(s,2,-1))