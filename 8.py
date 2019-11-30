#-*- coding:utf-8 -*-

#旋转数组最小的数字
def minNumberInRotateArray(rotateArray):
    #定义两个指针，一开始指针分别指向第一个和最后一个数字
    p1=0
    p2=len(rotateArray)-1
    index=p1   #初始化最小值的下标为第一个数字，因为可能数组旋转之后还是它本身，这个时候直接返回第一个值
    while rotateArray[p1]>=rotateArray[p2]:
        if p2-p1==1:
            return rotateArray[p2]
        index=(p1+p2)/2
        if rotateArray[p1]==rotateArray[p2] and rotateArray[p1]==rotateArray[index]:
            return Minorder(rotateArray,p1,p2)
        if rotateArray[index]>=rotateArray[p1]:
            p1=index
        elif rotateArray[index]<=rotateArray[p2]:
            p2=index

    return rotateArray[index]

def Minorder(rotateArray,left,right):
    '''
    当出现一种情况，p1,p2,index三者对应的值相等的时候，无法判断index对应的值属于前半部分还是后半部分
    这个时候只能用顺序查找
    :param rotateArray:
    :param left:
    :param right:
    :return:
    '''
    min=left
    for i in range(left,right+1):
        if rotateArray(i)<rotateArray(min):
            min=i
    return rotateArray[min]


if __name__=='__main__':

    array=[3,4,5,1,2]
    print(minNumberInRotateArray(array))