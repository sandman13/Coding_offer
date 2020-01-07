# -*- coding:utf-8 -*-


#请实现一个函数用来判断字符串是否表示数值（包括整数和小数）
#5e2也是数值，但是12e就不是
class Solution:
        # s字符串
        def isNumeric(self, s):
            # write code here
            if s is None or len(s) == 0:
                return False

            # 是否有e
            hasE = False
            # 是否有小数
            isDecimal = False
            # 是否有+-符号
            hasSign = False

            for i in range(len(s)):
                # 如果有e,只能有一个e且不能是最后一个
                if s[i] == "e" or s[i] == "E":
                    if hasE or i == len(s) - 1:
                        return False
                    hasE = True
                # 小数点不能重复出现或和e共线
                elif s[i] == ".":
                    if hasE or isDecimal:
                        return False
                    isDecimal = True
                elif s[i] == "-" or s[i] == "+":
                    # 重复出现符号时，必须跟在e后面
                    if hasSign and s[i - 1] != "e" and s[i - 1] != "E":
                        return False
                    # 重复出现符号时，必须跟在e后面
                    if not hasSign and i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                        return False
                    hasSign = True
                elif s[i] < "0" or s[i] > "9":
                    return False
            return True


if __name__=='__main__':
    s=Solution()
    str="100"
    print(s.isNumeric(str))
