#-*- coding:utf-8 -*-

#调整数组顺序使得奇数位于偶数前面

class Solution:

    def reOrderArray(self, array):
        '''
        这种方法会使得结果的顺序没有按照原本数出现的顺序排列
        :param array:
        :return:
        '''
        # write code here
        if array==None or len(array)==0:
            return
        p1=0  #从前向后的指针
        p2=len(array)-1  #从后向前的指针
        while(p1<p2):
            while(p1<p2 and array[p1]%2!=0):  #是奇数，则一直往后找
                p1+=1
            while(p1<p2 and array[p2]%2==0):
                p2-=1

            if p1<p2:
                temp=array[p1]
                array[p1]=array[p2]
                array[p2]=temp
        return array



    def test(self,array):
        '''
        学习用lambda解决问题
        :param array:
        :return:
        '''
        return sorted(array, key=lambda c: c % 2, reverse=True)


if __name__=='__main__':
    array=[1,2,3,4,5]
    re=Solution()
    print(re.reOrderArray(array))