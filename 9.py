#-*-coding:utf-8 -*-

import numpy as np
#实现斐波那契数列的实用解法
def Fibonacci(n):
    if n<2:
        return n
    fn_1=1
    fn_2=0
    for i in range(2,n+1):
        fn=fn_1+fn_2
        fn_2=fn_1
        fn_1=fn
    return fn


#青蛙跳台阶：一次跳1级或者2级，斐波那契数列的应用
def jumpFloor(number):
    if number==1:
        return number
    res=[0,1,2]
    for i in range(3,number+1):
        res.append(res[i-1]+res[i-2])
    return res[-1]

#变态跳台阶：一次可以跳任意多级，求青蛙上一个n级台阶的走法？
def jumpFloorII(number):
    #fn=fn_1+fn_2+...+f1 fn_1=fn_2+fn_3+...+f1 两式相减，得到fn=2fn_1,通过数学归纳法，fn=2^(n-1)
    num=1
    for i in range(2,number+1):
        num=2*num
    return num


def rectCover(number):
    '''
    矩阵覆盖:我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
    请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
    :param number:
    :return:
    '''
    if number<2:
        return number
    result=[0,1,2]
    for i in range(3,number+1):
        result.append(result[i-1]+result[i-2])
    return result[-1]


if __name__=='__main__':
    print(rectCover(8))