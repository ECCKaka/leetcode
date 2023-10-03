"""
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums. 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 

Constraints:

n == nums.length
1 <= n <= 10^5
1 <= nums[i] <= n
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # for num in nums:
        #     i = abs(num)-1
        #     nums[i] = abs(nums[i]) * (-1)
        #     print(nums[i])

        # print(nums)
        # result = []
        # for i, num in enumerate(nums):
        #     if num > 0:
        #         result.append(i+1)

        # return result
        s = set(nums)
        print(s)
        result = []

        for i in range(1, len(nums)+1):
            if i not in s:
                result.append(i)
        return result
