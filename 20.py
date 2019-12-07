#-*- coding:utf-8 -*-

#顺时针打印数组


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        if matrix == None:
            return result

        # 定义4个指针，上下左右
        up = 0
        down = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while (True):
            # 从左向右
            for i in range(left, right + 1):
                result.append(matrix[up][i])
            up += 1
            # 判断是否越界
            if up > down:
                break
            # 从上往下
            for i in range(up, down + 1):
                result.append(matrix[i][right])

            right -= 1
            if left > right:
                break
            # 从右往左：
            for i in range(right, left - 1, -1):
                result.append(matrix[down][i])

            down -= 1
            if up > down:
                break

            # 从下往上
            for i in range(down, up - 1, -1):
                result.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return result


if __name__=='__main__':
    s=Solution()
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(s.printMatrix(matrix))
