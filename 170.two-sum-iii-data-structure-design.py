#
# [170] Two Sum III - Data structure design
#
# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
#
# algorithms
# Easy (28.39%)
# Total Accepted:    47.4K
# Total Submissions: 166.9K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# Design and implement a TwoSum class. It should support the following
# operations: add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the
# value.
# 
# Example 1:
# 
# 
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# 
# 
# Example 2:
# 
# 
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false
# 
#
class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.s:
            self.s[number] = 1
        else:
            self.s[number] += 1
        
        

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """

        if len(self.s) == 0:
            return False
        
        for k, v in self.s.iteritems():
            u = value - k
            if u != k:
                if u in self.s:
                    return True
            else:
                if u in self.s and self.s[u] > 1:
                    return True
        return False
        
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
