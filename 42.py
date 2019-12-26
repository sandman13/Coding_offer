# -*- coding:utf-8 -*-


#翻转单词顺序 I am a student.   student. a am I
#思路：先将整个字符串翻转，然后再对每个单词做一次翻转

class Solution:
    def ReverseSentence(self, s):
        if len(s)<=1:
            return s
        s=s[::-1]   #[起始位置：最终位置：步长]，这里步长为-1则代表从后往前输出
        print(s)
        result=s.split(" ")
        temp=''
        for word in result:
            temp+=word[::-1]
            temp+=' '
        return temp[:-1]


    def LeftRotateString(self, s, n):
        '''
        字符串的左旋转操作
        :param s:
        :param n:
        :return:
        '''
        s=s[::-1]  #翻转整个字符串
        left=s[:len(s)-n]
        right=s[len(s)-n:]
        left=left[::-1]
        right=right[::-1]
        return left+right

if __name__=='__main__':
   s=Solution()
   sentence='I am a student.'
   sen2='abcdefg'
   print(s.LeftRotateString(sen2,2))