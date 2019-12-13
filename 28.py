#-*- cpoding:utf-8 -*-

#字符串的排列

class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res = []
        self.helper(ss, res, '')
        return sorted(list(set(res)))

    def helper(self, ss, res, path):
        if not ss:
            res.append(path)
        else:
            for i in range(len(ss)):
                self.helper(ss[:i] + ss[i+1:], res, path + ss[i])
