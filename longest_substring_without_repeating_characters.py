'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        astring = ""
        length = int(len(s))
        bstring = ""
        #print(length)
        
        if length==0 or length == 1:
            return length
        
        else:
             
            for i in range(length):
                
                if s[i] in astring:
                    pos = astring.index(s[i])
                    astring = astring[pos+1:]
                    #print astring
                    astring = astring + s[i]
                    #print astring
                    
                #print astring
                if s[i] not in astring:
                    
                    astring = astring + s[i]
                    
                
                if len(astring) > len(bstring):
                    bstring = astring
                    
                
                   
                        
            #print bstring            
            return len(bstring)
                
                
   
            
            
