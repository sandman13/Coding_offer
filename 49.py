# -*- coding:utf-8 -*-

#将字符串变为整数，如果不能转换则返回0

class Solution:
    def StrToInt(self, s):
        if s is None or len(s)==0:
            return 0
        sum=0
        flag=1   #标记是正数还是负数
        for i in range(0,len(s)):
            if i==0 and s[i]=='+':
                flag=True
                continue
            if i==0 and s[i]=='-':
                flag=-1
                continue
            if s[i]>='1' and s[i]<='9':
                sum=sum*10+int(s[i])
            else:
                return 0

        if -0x80000000 <= sum * flag <= 0x7FFFFFFF:
            return sum * flag
        else:
            return 0


if __name__=='__main__':
    s=Solution()
    str='12345'
    print(s.StrToInt(str))

