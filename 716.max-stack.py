#
# [716] Max Stack
#
# https://leetcode.com/problems/max-stack/description/
#
# algorithms
# Easy (38.15%)
# Total Accepted:    11.6K
# Total Submissions: 30.4K
# Testcase Example:  '["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]\n[[],[5],[1],[5],[],[],[],[],[],[]]'
#
# Design a max stack that supports push, pop, top, peekMax and popMax.
# 
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you
# find more than one maximum elements, only remove the top-most one.
# 
# 
# 
# Example 1:
# 
# MaxStack stack = new MaxStack();
# stack.push(5); 
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# 
# 
# 
# Note:
# 
# -1e7 
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.
# 
# 
#
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.max_vs = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.s.append(x)
        if len(self.max_vs) < 1:
            self.max_vs.append(x)
        elif x >= self.max_vs[-1]:
            self.max_vs.append(x)
        else:
            for i, v in enumerate(self.max_vs):
                if x < v:
                    break
            self.max_vs.insert(i, x)

    def pop(self):
        """
        :rtype: int
        """
        if self.s:
            p = self.s.pop(-1)
            for i, v in enumerate(self.max_vs):
                if v == p:
                    self.max_vs.pop(i)
                    break
            return p
        else:
            return None
        

    def top(self):
        """
        :rtype: int
        """
        if self.s:
            return self.s[-1]
        else:
            return None
        

    def peekMax(self):
        """
        :rtype: int
        """
        if len(self.max_vs) > 0:
            return self.max_vs[-1]
        else:
            return None
        
    def popMax(self):
        """
        :rtype: int
        """
        if self.max_vs:
            p = self.max_vs.pop(-1)
            for i in range(len(self.s)-1, -1, -1):
                if self.s[i] == p:
                    self.s.pop(i)
                    break
            return p
        else:
            return None
                

        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
