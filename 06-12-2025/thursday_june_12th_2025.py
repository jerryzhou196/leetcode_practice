import heapq

class Solution:
    def robotWithString(self, s: str) -> str:
        nice = [] 
        ans = ""

        rev = s[::-1]
        
        for index, char in enumerate(rev):
            heapq.heappush(nice, (char, index))

        n = len(rev)
        min_index = n


        
        while nice:
            char, idx = heapq.heappop(nice)
            if idx < min_index:
                ans += rev[idx:min_index]
                min_index = min(min_index, idx)
        
        return ans
            

s = Solution()
print(s.robotWithString("bac"))









    
        