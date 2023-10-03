"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str_dict = {}
        for i in s:
            str_dict[i] = str_dict.get(i, 0) + 1

        for k in t:
            str_dict[k] = str_dict.get(k, 0) - 1

        for i in str_dict:
            if str_dict[i] != 0:
                return False
        return True
