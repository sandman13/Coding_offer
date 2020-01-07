# -*- coding:utf-8 -*-


#字符流中第一个不重复的字符

class Solution:
    class Solution:
        # 返回对应char
        def __init__(self):
            self.charlist = []

        def FirstAppearingOnce(self):
            # write code here
            for key in self.charlist:
                if self.charlist.count(key) == 1:
                    return key
            return '#'

        def Insert(self, char):
            # write code here
            self.charlist.append(char)