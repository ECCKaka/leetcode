#
# 反转字符串
# 写出一个程序，接受一个字符串，然后输出该字符串反转后的字符串。（字符串长度不超过1000）
# 输入：
# "abcd"
# 返回值：
# "dcba"
# @param str string字符串 
# @return string字符串
#
class Solution:
    def solve(self , str ):
        # write code here
        result = ""
        for i in range(len(str), 0, -1):
            result += str[i-1]
        return result