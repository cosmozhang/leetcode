#
# [251] Flatten 2D Vector
#
# https://leetcode.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (42.78%)
# Total Accepted:    47.9K
# Total Submissions: 111.5K
# Testcase Example:  '[[1,2],[3],[4,5,6]]'
#
# Implement an iterator to flatten a 2d vector.
# 
# Example:
# 
# 
# Input: 2d vector =
# [
# ⁠ [1,2],
# ⁠ [3],
# ⁠ [4,5,6]
# ]
# Output: [1,2,3,4,5,6]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,2,3,4,5,6].
# 
# Follow up:
# As an added challenge, try to code it using only iterators in C++ or
# iterators in Java.
# 
#
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        if len(vec2d)>0:
            self.ls = reduce(lambda x,y: x+y, vec2d)
        else:
            self.ls = []
        self.idx = 0

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            ret = self.ls[self.idx]
            self.idx += 1
            return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx < len(self.ls):
            return True
        else:
            return False
        

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
