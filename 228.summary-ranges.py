#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (34.02%)
# Total Accepted:    114.4K
# Total Submissions: 336K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
# 
# Example 1:
# 
# 
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# 
# 
# Example 2:
# 
# 
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
# 
# 
#
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        
        ret_ls = []
        e_v = nums[0]
        s_v = nums[0]
        for num in nums[1:]:
            if num - e_v == 1:
                e_v = num
            else:
                if s_v == e_v:
                    ret_ls.append(str(s_v))
                else:
                    ret_ls.append(str(s_v)+'->'+str(e_v))
                s_v = num
                e_v = num
        if s_v == e_v:
            ret_ls.append(str(s_v))
        else:
            ret_ls.append(str(s_v)+'->'+str(e_v))
        return ret_ls
