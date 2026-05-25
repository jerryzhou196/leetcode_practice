class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        inserted = False 
        if not intervals: return [newInterval]

        for interval in intervals: 
            if not inserted and newInterval[0] < interval[0]: 
                ans.append(newInterval)
                inserted = True
            ans.append(interval)
        
        if not inserted:
            ans.append(newInterval)
        
        ans2 = [ans[0]]
        for interval in ans:
            if ans2[-1][1] >= interval[0]: 
                ans2[-1][1] = max(interval[1], ans2[-1][1])
            else:
                ans2.append(interval)
    
        return ans2


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        ans = []
         
        while i < n and intervals[i][1] < newInterval[0]: 
            ans.append(intervals[i])
            i += 1
        
        while i < n and intervals[i][0] <= newInterval[1]: 
            newInterval[1] = max(newInterval[1], intervals[i][1])
            newInterval[0] = min(newInterval[0], intervals[i][0])
            i += 1
        ans.append(newInterval)
        
        while i < n:
            ans.append(intervals[i])
            i += 1
    
        return ans
