class Solution:
    def isValid(self, s: str) -> bool:
        alist = []
        opening = ["(", "{", "["]
        closing = [")", "}", "]"]
        alist = []
        if len(s) == 0 or len(s) % 2 == 1:
            return False
        for i in s:
            if i in opening:
                alist.append(i)
            elif i in closing and len(alist) > 0:
                open_bracket = alist.pop()
                if open_bracket not in opening or opening.index(open_bracket) != closing.index(i):
                    return False
            else:
                return False
        if len(alist) == 0:
            return True
        return False


sol = Solution()
print(sol.isValid("]["))
