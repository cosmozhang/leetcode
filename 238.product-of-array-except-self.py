#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (51.97%)
# Total Accepted:    189.1K
# Total Submissions: 362.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        '''
        if not nums:
            return []
        if len(nums) == 1:
            return [0]
        
        forward_ls = []
        backward_ls = []

        prod_f = 1
        for num in nums:
            prod_f = prod_f*num
            forward_ls += [prod_f]

        prod_b = 1
        for num in nums[::-1]:
            prod_b = prod_b*num
            backward_ls += [prod_b]
        backward_ls = backward_ls[::-1]

        ret_ls = [None] * len(nums)
        ret_ls[0] = backward_ls[1]
        ret_ls[-1] = forward_ls[-2]
        for i in range(1, len(nums)-1):
            ret_ls[i] = forward_ls[i-1] * backward_ls[i+1]

        return ret_ls
        '''

        '''
        if len(nums) == 1:
            return 0

        f_prods = []
        b_prods = []

        p = 1
        for num in nums:
            p *= num
            f_prods.append(p)

        p = 1
        for num in nums[::-1]:
            p *= num
            b_prods.append(p)
        b_prods = b_prods[::-1]

        res_ls = [None for _ in range(len(nums))]
        for idx in range(len(nums)):
            if idx == 0:
                res_ls[idx] = b_prods[1]
            elif idx == len(nums) - 1:
                res_ls[idx] = f_prods[-2]
            else:
                res_ls[idx] = f_prods[idx-1] * b_prods[idx+1]
        return res_ls
        '''
        if len(nums) == 1:
            return 0

        zcnt = 0
        p = 1
        for num in nums:
            if num != 0:
                p *= num
            else:
                zcnt += 1

        res_ls = [None for _ in range(len(nums))]

        for idx in range(len(nums)):
            if zcnt > 1:
                res_ls[idx] = 0
            elif zcnt == 1:
                if nums[idx] == 0:
                    res_ls[idx] = p
                else:
                    res_ls[idx] = 0
            else:
                res_ls[idx] = p/nums[idx]
            

        return res_ls
