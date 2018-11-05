#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (35.22%)
# Total Accepted:    20.3K
# Total Submissions: 57.5K
# Testcase Example:  '[1,1,2,2,2]'
#
# Remember the story of Little Match Girl? By now, you know exactly what
# matchsticks the little match girl has, please find out a way you can make one
# square by using up all those matchsticks. You should not break any stick, but
# you can link them up, and each matchstick must be used exactly one time.
# 
# ⁠Your input will be several matchsticks the girl has, represented with their
# stick length. Your output will either be true or false, to represent whether
# you could make one square using all the matchsticks the little match girl
# has.
# 
# Example 1:
# 
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
# 
# 
# 
# Example 2:
# 
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
# 
# 
# 
# Note:
# 
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
# 
# 
#
class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1:
            return False

        if sum(nums)%4 != 0:
            return False

        t = sum(nums)/4
        
        nums.sort(reverse=True)
        if nums[0] > t:
            return False

        sums = [0 for _ in range(4)]

        return self.helper(nums, sums, 0, t)
        
    def helper(self, nums, sums, idx, t):
        
        if idx == len(nums):
            return sums[0] == t and sums[1] == t and sums[2] == t

        for i in range(4):
            if sums[i]+nums[idx] > t:
                continue
            sums[i] += nums[idx]
            if self.helper(nums, sums, idx+1, t):
                return True
            sums[i] -= nums[idx]
            
        return False
