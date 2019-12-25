#-*- coding:utf-8 -*-

#统计一个数字在排序数组中出现的次数

#因为是一个排序数组，所以首先想到是用二分搜索的方式
#为了找到这个数字出现的次数，就需要定位这个数字第一次出现的下标和最后一次出现的下标


def getFirst(data,k,start,end):
    '''
    获取第一次出现的下标
    :param data:
    :param k:
    :param start:
    :param end:
    :return:
    '''
    if start>end:
        return -1
    mid=(start+end)/2
    if data[mid]==k:
        #如果中间数正好等于k,并且前一个数不为k或者mid==0，那么说明此时就是第一个k
        if (mid>0 and data[mid-1]!=k) or (mid==0):
            return mid
        else:
            #否则第一个k肯定还在前半段
            end=mid-1
    elif data[mid]>k:
        end=mid-1
    else:
        start=mid+1
    return getFirst(data,k,start,end)


def getLast(data,k,start,end):
    '''
    获取数字最后一次出现的位置
    :param data:
    :param k:
    :param start:
    :param end:
    :return:
    '''
    if start>end:
        return -1
    mid=(start+end)/2
    if data[mid]==k:
        #如果中间数正好等于k,并且后一个数不为k或者mid是最后，那么说明此时就是最后一个k
        if (mid<len(data)-1 and data[mid+1]!=k) or (mid==len(data)-1):
            return mid
        else:
            #否则最后一个k肯定还在后半段
            start=mid+1
    elif data[mid]>k:
        end=mid-1
    else:
        start=mid+1
    return getLast(data,k,start,end)

def GetNumberOfK(data, k):
    num=0
    if data is not None and len(data)>0:
        first_index=getFirst(data,k,0,len(data)-1)
        last_index=getLast(data,k,0,len(data)-1)
        if first_index>-1 and last_index>-1:
            num=last_index-first_index+1
    return num


if __name__=='__main__':
    data=[1,2,3,3,3,3,4,5]
    print(GetNumberOfK(data,3))