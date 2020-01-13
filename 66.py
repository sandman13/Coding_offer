# -*- coding:utf-8 -*-


#矩阵中的路径

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        assistMatrix = [True]*rows*cols
        for i in range(rows):
            for j in range(cols):
                if(self.hasPathAtAStartPoint(matrix,rows,cols, i, j, path, assistMatrix)):
                    return True
        return False
    def hasPathAtAStartPoint(self, matrix, rows, cols, i, j, path, assistMatrix):
        if not path:
            return True
        index = i*cols+j
        if i<0 or i>=rows or j<0 or j>=cols or matrix[index]!=path[0] or assistMatrix[index]==False:
            return False
        assistMatrix[index] = False
        if(self.hasPathAtAStartPoint(matrix,rows,cols,i+1,j,path[1:],assistMatrix) or self.hasPathAtAStartPoint(matrix,rows,cols,i-1,j,path[1:],assistMatrix) or self.hasPathAtAStartPoint(matrix,rows,cols,i,j-1,path[1:],assistMatrix) or self.hasPathAtAStartPoint(matrix,rows,cols,i,j+1,path[1:],assistMatrix)):
            return True
        assistMatrix[index] = True
        return False

if __name__=='__main__':
    s=Solution()
    print(s.hasPath([1,2,3,4,5,6,7,8,9,10,11,12],3,4,[1,2,3,4,5]))