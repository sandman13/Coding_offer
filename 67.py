# -*- coding:utf-8 -*-

#机器人的运动范围

#地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
# 但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
# 但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？

class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        matrix = [[0 for i in range(cols)] for j in range(rows)]
        count = self.find_index(threshold, rows, cols, matrix, 0, 0)
        print(matrix)
        return count


    def find_index(self,threshold,rows,cols,matrix,i,j):
        count=0
        if i<rows and j<cols and i>=0 and j>=0 and self.cal_sum(i,j,threshold) and matrix[i][j]==0:
            matrix[i][j]=1
            count=1+self.find_index(threshold,rows,cols,matrix,i+1,j) \
                   +self.find_index(threshold,rows,cols,matrix,i-1,j)\
                   +self.find_index(threshold,rows,cols,matrix,i,j-1)\
                   +self.find_index(threshold,rows,cols,matrix,i,j+1)
        return count



    def cal_sum(self,index1,index2,threshold):
        '''
        计算对应下标的数位之和,并且和阙值进行比较
        :param index1:
        :param index2:
        :param threshold:
        :return:
        '''
        #sum(map(int, str(i) + str(j))  这一句话直接得到位数之和
        sum=0
        while index1>0:
          sum+=index1%10
          index1/=10
        while index2>0:
            sum+=index2%10
            index2/=10
        if sum<=threshold:
            return True
        else:
            return False



if __name__=='__main__':
    s=Solution()
    print(s.movingCount(9,12,12))