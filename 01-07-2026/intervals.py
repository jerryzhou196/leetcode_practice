class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        ans = []
        curr_interval = intervals[0] if intervals else []

        for interval in intervals[1:]:
            if interval[0] <= curr_interval[1]:
                curr_interval[1] = max(interval[1], curr_interval[1])
            else: 
                ans.append(curr_interval)
                curr_interval = interval

        ans.append(curr_interval)
        return ans


        