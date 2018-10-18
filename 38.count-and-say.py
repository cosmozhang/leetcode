#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (38.02%)
# Total Accepted:    226.5K
# Total Submissions: 595.3K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        ls = []

        for i in range(1, n+1):
            if i == 1:
                ls.append('1')
            else:
                item = ls[-1]
                new_item = ''
                tmp = []
                for j in range(len(item)):
                    if j == 0:
                        tmp = [item[j]]
                    elif j > 0 and item[j] == item[j-1]:
                        tmp += [item[j]]
                    else:
                        new_item += str(len(tmp))+str(tmp[0])
                        tmp = [item[j]]
                new_item += str(len(tmp))+str(tmp[0])
                ls.append(new_item)

        return ls[-1]
