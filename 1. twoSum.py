'''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # self.next = 1

        # for i in range(0,len(nums)):

        #     for j in range(self.next,len(nums)):
        #         #print len(nums)-1
        #         if (nums[i] + nums[j]) == target:
        #             return i,j

        #     self.next += 1
        #     if self.next == len(nums):
        #         break

        # 2023, Oct 3rd
        hashMap = {}

        for i, num in enumerate(nums):
            print(i, num)
            diff = target-num
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[num] = i
        return []
