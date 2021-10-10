#
# 旋转数组
# @param n int整型 数组长度
# @param m int整型 右移距离
# @param a int整型一维数组 给定数组
# @return int整型一维数组
#
class Solution:
    def solve(self , n , m , a ):
        # write code here
        if m == 0: return a
        else:
            for _ in range(m):
                last = a.pop(-1)
                a.insert(0, last)
            return a
#             new_a = [None] * n
#             for i in range(n):
#                 new_a[(i+m)%n] = a[i]
#             return new_a
