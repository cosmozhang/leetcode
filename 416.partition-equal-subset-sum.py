#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (38.88%)
# Total Accepted:    60.9K
# Total Submissions: 156.5K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
# 
# 
# Note:
# 
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# 
# 
# 
# Example 1:
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# 
# Example 2:
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
#
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        
        if sum(nums) % 2 !=0:
            return False

        t = sum(nums)/2

        tb = set()
        tb.add(0)


        for num in nums:
            for v in tb.copy():
                tb.add(v+num)

        if t in tb:
            return True
        return False
