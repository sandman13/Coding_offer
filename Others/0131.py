#-*- coding:utf-8 -*-
from decimal import Decimal



#01矩阵求解连通域：DFS


n,m=map(int,input().split())
#print(type(n))
matrix = []
for _ in range(n):
    temp=input().split(' ')
    matrix.append(temp)
#print(matrix)
# 定义上下左右对角线的方位
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
res = 0

def dfs(i, j,temp):
    temp[0]+=1
    temp[1]+=j
    temp[2]+=i
    matrix[i][j] = 0
    for k in range(len(dx)):
        x, y = i + dx[k], j + dy[k]
        if x>=0 and y>=0 and x<n and y<m and matrix[x][y] == '1':
            dfs(x, y,temp)
#记录每个连通域的面积和横纵坐标
result=[]

for i in range(n):
    for j in range(m):
        if matrix[i][j]=='1':
            res += 1
            #分别是面积，纵坐标，横坐标
            temp=[0,0,0]
            dfs(i,j,temp)
            #得到横纵坐标的平均值，保留两位小数
            temp[1]=str(Decimal(temp[1]/temp[0]).quantize(Decimal('0.00')))
            temp[2]=str(Decimal(temp[2] / temp[0]).quantize(Decimal('0.00')))
            result.append(temp)

print(res)
for i in range(len(result)):
    print("%d %s %s" %(result[i][0],result[i][1],result[i][2]))
