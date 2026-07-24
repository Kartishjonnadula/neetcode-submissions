class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        ans=0
        i=0
        while i<(len(intervals)-1):
            x1,y1=intervals[i]
            x2,y2=intervals[i+1]
            if x2<y1:
                if y2>y1:
                    intervals[i],intervals[i+1]=intervals[i+1],intervals[i]
                ans+=1
            i+=1
        return ans
