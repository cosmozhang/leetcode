#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (57.41%)
# Total Accepted:    60.8K
# Total Submissions: 105.9K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
# 
# 
# Note:
# The number of people is less than 1,100.
# 
# 
# 
# 
# Example
# 
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# 
#
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        ret_ls = []

        def ccmp(a, b):
            if a[0]!=b[0]:
                return a[0] - b[0]
            else:
                return -(a[1] - b[1])


        people.sort(cmp=ccmp, reverse = True)

        for person in people:
            ret_ls.insert(person[1], person)
        return ret_ls
        
                            
        
        
