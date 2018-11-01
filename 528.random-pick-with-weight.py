#
# [912] Random Pick with Weight
#
# https://leetcode.com/problems/random-pick-with-weight/description/
#
# algorithms
# Medium (41.42%)
# Total Accepted:    6.8K
# Total Submissions: 16.4K
# Testcase Example:  '["Solution", "pickIndex"]\n[[[1]], []]'
#
# Given an array w of positive integers, where w[i] describes the weight of
# index i, write a function pickIndex which randomly picks an index in
# proportion to its weight.
# 
# Note:
# 
# 
# 1 <= w.length <= 10000
# 1 <= w[i] <= 10^5
# pickIndex will be called at most 10000 times.
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array w. pickIndex has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
# 
#
import random
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.cum = [None] * len(w)
        self.cum[0] = w[0]
        
        for i in range(1, len(w)):
            self.cum[i] = self.cum[i-1]+w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        sample = random.randint(1, self.cum[-1])
        l = 0
        r = len(self.cum)-1
        while l + 1 < r:
            m = (l+r)/2
            if self.cum[m] <= sample:
                l = m
            elif sample < self.cum[m]:
                r = m

        if sample <= self.cum[l]:
            return l
        return r
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
