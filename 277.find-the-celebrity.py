#
# [277] Find the Celebrity
#
# https://leetcode.com/problems/find-the-celebrity/description/
#
# algorithms
# Medium (35.07%)
# Total Accepted:    63.8K
# Total Submissions: 181.8K
# Testcase Example:  '0 does not know 1; 1 does not know 0.'
#
# 
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among
# them, there may exist one celebrity. The definition of a celebrity is that
# all the other n - 1 people know him/her but he/she does not know any of
# them.
# 
# 
# 
# Now you want to find out who the celebrity is or verify that there is not
# one. The only thing you are allowed to do is to ask questions like: "Hi, A.
# Do you know B?" to get information of whether A knows B. You need to find out
# the celebrity (or verify there is not one) by asking as few questions as
# possible (in the asymptotic sense).
# 
# 
# 
# You are given a helper function bool knows(a, b) which tells you whether A
# knows B. Implement a function int findCelebrity(n), your function should
# minimize the number of calls to knows.
# 
# 
# 
# Note: There will be exactly one celebrity if he/she is in the party. Return
# the celebrity's label if there is a celebrity in the party. If there is no
# celebrity, return -1.
# 
#
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        if n == 0 or n == 1:
            return -1

        candidate = 0

        for i in range(1, n):
            if knows(candidate, i):
                candidate = i

        for i in range(n):
            if i != candidate:
                if (knows(candidate, i) or not knows(i, candidate)):
                    return -1

        return candidate
        '''

        if n == 0 or n == 1:
            return -1

        cand = 0

        for i in range(1, n):
            if knows(cand, i):
                cand = i

        for i in range(0, n):
            if i != cand:
                if knows(cand, i) or not knows(i, cand):
                    return -1
        return cand
