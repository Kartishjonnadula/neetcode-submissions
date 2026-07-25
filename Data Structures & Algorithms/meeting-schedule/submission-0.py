"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals=[(interval.start,interval.end) for interval in intervals]
        intervals.sort()
        prev=intervals[0][1]
        for start,end in intervals[1:]:
            if prev>start:
                return False
            prev=end
        return True
