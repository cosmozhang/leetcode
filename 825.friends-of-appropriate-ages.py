#
# [852] Friends Of Appropriate Ages
#
# https://leetcode.com/problems/friends-of-appropriate-ages/description/
#
# algorithms
# Medium (33.99%)
# Total Accepted:    11.3K
# Total Submissions: 33.4K
# Testcase Example:  '[16,16]'
#
# Some people will make friend requests. The list of their ages is given and
# ages[i] is the age of the ith person. 
# 
# Person A will NOT friend request person B (B != A) if any of the following
# conditions are true:
# 
# 
# age[B] <= 0.5 * age[A] + 7
# age[B] > age[A]
# age[B] > 100 && age[A] < 100
# 
# 
# Otherwise, A will friend request B.
# 
# Note that if A requests B, B does not necessarily request A.  Also, people
# will not friend request themselves.
# 
# How many total friend requests are made?
# 
# Example 1:
# 
# 
# Input: [16,16]
# Output: 2
# Explanation: 2 people friend request each other.
# 
# 
# Example 2:
# 
# 
# Input: [16,17,18]
# Output: 2
# Explanation: Friend requests are made 17 -> 16, 18 -> 17.
# 
# Example 3:
# 
# 
# Input: [20,30,100,110,120]
# Output: 
# Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 ->
# 100.
# 
# 
# 
# 
# Notes:
# 
# 
# 1 <= ages.length <= 20000.
# 1 <= ages[i] <= 120.
# 
# 
#
class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        
        q_sum = 0
        '''
        for idx_A, age_A in enumerate(ages):
            for idx_B, age_B in enumerate(ages):
                if idx_A == idx_B or (age_B <= 0.5*age_A+7) or (age_B > age_A) or (age_B > 100 and age_A < 100):
                    continue
                else:
                    q_sum += 1
        return q_sum
        '''
        
        ages.sort()
        for idx, age in enumerate(ages):
            l, r = 0, idx
            t = age*0.5 + 7
            while l < r:
                m = (l+r) >> 1
                if ages[m] <= t:
                    l = m+1
                else:
                    r = m
            q_sum += idx - r
            if age > 14:
                l, r = idx, len(ages)-1
                t = age
                while l < r:
                    m = (l+r) >> 1
                    if ages[m] > t:
                        r = m
                    else:
                        l = m+1
                q_sum += l - idx-1 if ages[l] > t  else l - idx

        return q_sum
                    
