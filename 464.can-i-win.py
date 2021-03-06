#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (26.20%)
# Total Accepted:    28.4K
# Total Submissions: 108.2K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins. 
# 
# What if we change the game so that players cannot re-use integers? 
# 
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
# 
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally. 
# 
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
# 
# 
# Example
# 
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
# 
# 
#
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """

        memo = {}
        choosable = range(1, maxChoosableInteger+1)
        t = desiredTotal

        if any([x >= t for x in choosable]):
            return True
        if sum(choosable) < t:
            return False

        return self.helper(0, choosable, t, memo)



    def helper(self, c_sum, choosable, t, memo):
        
        if len(choosable) == 0:
            return False
        
        state = tuple(choosable)
        if state in memo:
            return memo[state]
        else:
            memo[state] = False
        
            for x in choosable:
                if c_sum + x >= t:
                    memo[state] = True
                    break
                else:
                    new_choosable = [y for y in choosable if y != x]
                    if not self.helper(c_sum + x, new_choosable, t, memo):
                        memo[state] = True
                        break

        return memo[state]
        
