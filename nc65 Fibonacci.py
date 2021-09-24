# -*- coding:utf-8 -*-
# 根据斐波那契数列的定义可知，
# fib(1)=1,fib(2)=1,
# fib(3)=fib(3-1)+fib(3-2)=2,
# fib(4)=fib(4-1)+fib(4-2)=3，
# 所以答案为4。  

class Solution:
    def Fibonacci(self, n):
        # write code here
#         print(n)
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        else:
            sum_num = 0
            f1 = 1
            f2 = 1
            
            for i in range(3,n+1):
                sum_num = f1+f2
                f1 = f2
                f2 = sum_num
            return sum_num