#
# [56] Merge Intervals
#
# https://leetcode.com/problems/merge-intervals/description/
#
# algorithms
# Medium (32.71%)
# Total Accepted:    232.9K
# Total Submissions: 707.7K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given a collection of intervals, merge all overlapping intervals.
# 
# Example 1:
# 
# 
# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        '''
        if not intervals:
            return []
        intervals = sorted(intervals, key=lambda x:x.start)
        ret_ls = [intervals[0]]
        new_idx = 0
        end = intervals[0].end
        for idx in range(1, len(intervals)):
            if intervals[idx].start <= end:
                if intervals[idx].end > end:
                    ret_ls[new_idx].end = intervals[idx].end
                    end = intervals[idx].end
            else:
                ret_ls.append(intervals[idx])
                end = intervals[idx].end
                new_idx += 1
        return ret_ls
        '''


        if len(intervals) == 0:
            return []
        
        ret_ls = []

        sorted_intervals = sorted(intervals, key = lambda x: x.start)

        c_end = sorted_intervals[0].end

        ret_ls.append(sorted_intervals[0])

        for interv in sorted_intervals[1:]:
            if interv.start > ret_ls[-1].end:
                ret_ls.append(interv)
            else:
                ret_ls[-1].end = max(c_end, interv.end)
            c_end = ret_ls[-1].end

        return ret_ls
        
        
