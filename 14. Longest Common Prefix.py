"""
    14. Longest Common Prefix - Easy 

    Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

    

    Example 1:

    Input: strs = ["flower","flow","flight"]
    Output: "fl"
    Example 2:

    Input: strs = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.
    

    Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        shortest = min(strs, key=len)

        if len(shortest) == 0:
            return ""
        lcp = ''
        for i in range(0, len(shortest)):
            lcp += shortest[i]
            for string in strs:
                if string[:i+1] != lcp and i < len(string):

                    return lcp[:len(lcp)-1]
        return lcp


sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
