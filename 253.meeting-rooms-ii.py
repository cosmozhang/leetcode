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

        '''
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
        '''
        if len(intervals) == 0:
            return 0
        
        tmp_ls = []

        for interv in intervals:
            tmp_ls.append((interv.start, 's'))
            tmp_ls.append((interv.end, 'e'))

        def cus_cmp(a, b):
            if a[0] < b[0]:
                return -1
            elif a[0] > b[0]:
                return 1
            else:
                if a[1] == 'e' and b[1] == 's':
                    return -1
                elif a[1] == 's' and b[1] == 'e':
                    return 1
                else:
                    return 0
            
        s_tmp_ls = sorted(tmp_ls, cmp = cus_cmp)

        max_rooms = 0
        rooms = 0
        for ts in s_tmp_ls:
            if ts[1] == 's':
                rooms += 1
            elif ts[1] == 'e':
                rooms -= 1
            max_rooms = max(max_rooms, rooms)

        return max_rooms
