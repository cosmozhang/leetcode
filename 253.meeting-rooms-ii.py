#
# [253] Meeting Rooms II
#
# https://leetcode.com/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (40.55%)
# Total Accepted:    99.4K
# Total Submissions: 245K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals consisting of start and end times
# [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
# required.
# 
# Example 1:
# 
# 
# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# 
# Example 2:
# 
# 
# Input: [[7,10],[2,4]]
# Output: 1
# 
#
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        
        start_ls = sorted([interval.start for interval in intervals])
        end_ls = sorted([interval.end for interval in intervals])

        max_room_num = 0
        end_idx = 0
        for idx in range(len(start_ls)):
            if start_ls[idx] < end_ls[end_idx]:
                max_room_num += 1
            else:
                end_idx += 1
        return max_room_num
