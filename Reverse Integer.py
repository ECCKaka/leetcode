'''
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
'''
def reverse( x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        n = x 
        x = x*(-1)
    reversed = 0    
    while(x > 0):    
        r = x % 10    
        reversed = (reversed * 10) + r    
        x = x //10    
    
    if n < 0:
        return str(reversed) + "-"

    return reversed

print reverse(-123)