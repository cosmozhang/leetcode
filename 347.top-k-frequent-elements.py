#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (51.57%)
# Total Accepted:    148K
# Total Submissions: 286.9K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        freq_dic = {}
        for num in nums:
            if num not in freq_dic:
                freq_dic[num] = 1
            else:
                freq_dic[num] += 1

        buckets = [[] for _ in range(len(nums)+1)]

        for key, v in freq_dic.iteritems():
            buckets[v] += [key]

        rev_buckets = buckets[::-1]

        res_ls = reduce(lambda x, y: x+y, rev_buckets)
        return res_ls[:k]
