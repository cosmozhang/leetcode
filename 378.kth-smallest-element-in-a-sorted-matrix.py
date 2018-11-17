#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (46.88%)
# Total Accepted:    81.9K
# Total Submissions: 174.6K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.
#
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        n = len(matrix)

        low, high = matrix[0][0], matrix[n-1][n-1]

        while low <= high:
            mid = (low+high) >> 1
            cand_k = self.helper(matrix, n, mid)
            if cand_k < k:
                low = mid + 1
            elif cand_k >= k:
                high = mid - 1

        return low


    def helper(self, matrix, n, v):

        c = 0
        r = n-1
        cnt_k = 0
        while c < n and r > -1:
            if matrix[r][c] <= v:
                c += 1
                cnt_k += (r+1)
            else:
                r -= 1

        return cnt_k
        
