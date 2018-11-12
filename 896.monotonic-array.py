#
# [932] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (54.60%)
# Total Accepted:    18.8K
# Total Submissions: 34.4K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
# 
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array
# A is monotone decreasing if for all i <= j, A[i] >= A[j].
# 
# Return true if and only if the given array A is monotonic.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,2,3]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [6,5,4,4]
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,3,2]
# Output: false
# 
# 
# 
# Example 4:
# 
# 
# Input: [1,2,4,5]
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: [1,1,1]
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
# 
# 
# 
# 
# 
# 
# 
#
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        
        if len(A) == 0 or len(A) == 1 or len(A)==2:
            return True

        s =0
        while s<len(A)-1 and A[s] == A[s+1]:
            s+=1
            
        if s == len(A)-1:
            return True
        else:
            if A[s]<A[s+1]:
                for i, a in enumerate(A):
                    if i>s and i<len(A)-1:
                        if a > A[i+1]:
                            return False
                return True
            elif A[s]>A[s+1]:
                for i, a in enumerate(A):
                    if i>s and i<len(A)-1:
                        if a < A[i+1]:
                            return False
                return True

                
                        
                            
