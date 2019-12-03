#-*- coding:utf-8 -*-

def NumberOf1(n):
    '''
    二进制中1的个数
    :param n:
    :return:
    '''
    count=0
    #首先看到题目会有两种思路，一个是将数每次右移一位，和1做与运算，但是当数为负数的时候会陷入死循环
    #所以，第二种思路是，就是左移1，每次都能和n的一位进行比较，但是python中int超过64之后，会转为长整型，所以会死循环
    #第三种思路：把一个整数减去1再和原整数做与运算，会把该整数最右边一个1变为0，那么二进制整数有几个1就会进行几次操作
    while(n&0xffffffff != 0):    #注意写法
        count+=1
        n=(n-1)&n
    return count



if __name__=='__main__':
    print(NumberOf1(9))