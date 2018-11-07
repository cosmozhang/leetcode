#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (56.35%)
# Total Accepted:    35.3K
# Total Submissions: 62.5K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        
        if len(T) ==1:
            return [0]

        ret_ls = [0 for _ in range(len(T))]
        s = [(0, T[0])]
        for idxm1, t in enumerate(T[1:]):
            idx = idxm1+1
            while len(s)>0 and t>s[-1][1]:
                old = s.pop(-1)
                ret_ls[old[0]] = idx - old[0]
            s.append((idx, t))
        return ret_ls
