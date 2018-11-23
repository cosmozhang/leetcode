#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Medium (22.78%)
# Total Accepted:    47.4K
# Total Submissions: 208.2K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
# Given a sorted integer array nums, where the range of elements are in the
# inclusive range [lower, upper], return its missing ranges.
# 
# Example:
# 
# 
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
# 
# 
#
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        if len(nums) == 0:
            if lower < upper:
                return [str(lower)+'->'+str(upper)]
            elif lower == upper:
                return [str(lower)]
        
        ret_ls = []
        if lower < nums[0]:
            if lower + 1 == nums[0]:
                ret_ls.append(str(lower))
            else:
                ret_ls.append(str(lower)+'->'+str(nums[0]-1))

        l = 0
        r = 1

        while r < len(nums):
            if nums[l] == nums[r]:
                l+=1
                r+=1
            elif nums[l] +1 == nums[r]:
                l += 1
                r += 1
            elif nums[l]+2 == nums[r]:
                ret_ls.append(str(nums[l]+1))
                l += 1
                r += 1
            else:
                ret_ls.append(str(nums[l]+1)+'->'+str(nums[r]-1))
                l += 1
                r += 1
                
        if nums[-1] < upper:
            if nums[-1]+1 == upper:
                ret_ls.append(str(upper))
            else:
                ret_ls.append(str(nums[-1]+1)+'->'+str(upper))

        return ret_ls
