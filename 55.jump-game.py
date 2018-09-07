#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (30.03%)
# Total Accepted:    190K
# Total Submissions: 630.5K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current_idx = 0
        best_idx = 0
        while True:
            jumps = nums[current_idx]
            if best_idx >= len(nums) - 1:
                return True
            elif jumps == 0 and current_idx < len(nums) - 1:
                return False

            old_current_idx = current_idx
            for jump in range(1, jumps+1):
                next_idx = old_current_idx + jump
                if next_idx >= len(nums) - 1:
                    return True
                new_best_idx = next_idx + nums[next_idx]
                if new_best_idx >= best_idx:
                    best_idx = new_best_idx
                    current_idx = next_idx
                
