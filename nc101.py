#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 找缺失数字
# @param a int整型一维数组 给定的数字串
# @return int整型
# 从 0,1,2,...,n 这 n+1 个数中选择 n 个数，
# 选择出的数字依然保持有序，找出这 n 个数中缺失的那个数，
# 要求 O(n) 或 O(log(n)) 并尽可能小。
# input:[0,1,2,3,4,5,7]
# output: 6
# input: [0,1,2,3,4,5,6,7]
# output: 8
# input:[0,2,3]
# output: 1

class Solution:
    def solve(self , a ):
        # write code here
        # divide 
        if a[-1] != len(a):
            return len(a)
        if a[0]!=0:
            return 0
        a_len = len(a)
        a_max = len(a)
        a_min = 0
        while a_min<=a_max:
            cur_index = (a_max-a_min)//2 + a_min
            left_str = a[a_min: cur_index]
            right_str = a[cur_index: a_max]
            if cur_index in left_str:
                a_max = cur_index
            elif cur_index in right_str:
                a_min = cur_index
            else:
                return cur_index