#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (57.64%)
# Total Accepted:    375.5K
# Total Submissions: 650.7K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
#
# Note:
#
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
#
# Example 1:
#
#
# Input: [2,2,1]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,1,2,1,2]
# Output: 4
#
# Bit operation is a better solution ^
#
class Solution(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d={}
        for x in A:
            if d.has_key(x):
                d[x]+=1
            else:
                d.setdefault(x, 1)
        for key in d:
            if d[key]==1:
                return key
                break
        return None

