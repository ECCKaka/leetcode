#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 
# @param str string字符串 待判断的字符串
# @return bool布尔型
# 输入：
# "absba"
# 返回值：
# true

# 输入：
# "yamatomaya"
# 返回值：
# false

# 输入：
# "a"
# 返回值：
# true
class Solution:
    def judge(self , str ):
        # write code here
        str_len = len(str)
        if str_len == 0 or str_len==1:
            return True
        else:
            half_len = str_len//2
            counter = -1
            for i in range(half_len):
                # print(str[i],str[counter])
                if str[i] != str[counter]:
                    return False
                counter -= 1
            return True