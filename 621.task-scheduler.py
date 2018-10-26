#
# [621] Task Scheduler
#
# https://leetcode.com/problems/task-scheduler/description/
#
# algorithms
# Medium (42.63%)
# Total Accepted:    54.4K
# Total Submissions: 127.2K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# Given a char array representing tasks CPU need to do. It contains capital
# letters A to Z where different letters represent different tasks.Tasks could
# be done without original order. Each task could be done in one interval. For
# each interval, CPU could finish one task or just be idle.
# 
# However, there is a non-negative cooling interval n that means between two
# same tasks, there must be at least n intervals that CPU are doing different
# tasks or just be idle.
# 
# You need to return the least number of intervals the CPU will take to finish
# all the given tasks.
# 
# 
# 
# Example:
# 
# 
# Input: tasks = ["A","A","A","B","B","B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
# 
# 
# 
# 
# Note:
# 
# 
# The number of tasks is in the range [1, 10000].
# The integer n is in the range [0, 100].
# 
# 
#
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        
        task_dic = {}
        for j in tasks:
            if j not in task_dic:
                task_dic[j] = 1
            else:
                task_dic[j] += 1

        sorted_task_dic = sorted(task_dic.iteritems(), key = lambda x: x[1], reverse=True)

        _, v_max = sorted_task_dic[0]
        c = 1
        for k, v in sorted_task_dic[1:]:
            if v == v_max:
                c += 1
            else:
                break
        return max((v_max-1)*(n+1)+c, sum([v for k, v in sorted_task_dic]))
