#
# [698] Partition to K Equal Sum Subsets
#
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/
#
# algorithms
# Medium (39.32%)
# Total Accepted:    26.5K
# Total Submissions: 67.4K
# Testcase Example:  '[4,3,2,3,5,2,1]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into k non-empty subsets whose sums are all
# equal.
# 
# Example 1:
# 
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3),
# (2,3) with equal sums.
# 
# 
# 
# Note:
# 1 .
# 0 < nums[i] < 10000.
# 
#
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        if len(nums) < k:
            return False
        
        if k == 1:
            return True
        
        if sum(nums) % k != 0:
            return False

        t = sum(nums)/k

        nums.sort(reverse = True)

        if any([num > t for num in nums]):
            return False
        sums= [0 for _ in range(k)]

        return self.helper(nums, sums, 0, t, k)


    def helper(self, nums, sums, idx, t, k):

        if idx == len(nums):
            return reduce(lambda x, y: x and y, [sums[i] == t for i in range(k-1)])

        for i in range(k):
            num = nums[idx]
            if sums[i] + num <= t:
                sums[i] += num
                if self.helper(nums, sums, idx+1, t, k):
                    return True
                sums[i] -= num

        return False
