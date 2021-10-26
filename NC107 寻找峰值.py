#
# 寻找最后的山峰
# @param a int整型一维数组 
# @return int整型
#
class Solution:
    def solve(self , a ):
        # write code here
        for i in range(len(a)-1, 0, -1):
            if(a[i]>=a[i-1]):
                return i
        return 0