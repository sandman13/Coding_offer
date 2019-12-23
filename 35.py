# -*- coding:utf-8 -*-

from collections import OrderedDict

#第一个只出现一次的字符

class Solution:
    def FirstNotRepeatingChar(self, s):
        if s is None or len(s)==0:
            return -1
        #利用hashmap存储
        temp=OrderedDict()
        for i in range(len(s)):
            if s[i] not in temp.keys():
                temp[s[i]]=1
            else:
                temp[s[i]]+=1

        for key in temp.keys():
            if temp[key]==1:
                print(key)
                return s.index(key)
        return -1

if __name__=='__main__':
    s=Solution()
    print(s.FirstNotRepeatingChar('google'))


