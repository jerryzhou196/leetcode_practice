import heapq

class Solution:
    def robotWithString(self, s: str) -> str:
        nice = [] 
        ans = ""

        rev = s[::-1]
        
        for index, char in enumerate(rev):
            heapq.heappush(nice, (char, index))

        n = len(rev)
        stack = []
        
        while stack:
            if nice:
                char, idx = heapq.heappop(nice)
                stack.append(rev[idx:n])
                if stack[len(stack) - 1] < char:


                

            else:
                ans += str(stack)


            if idx < min_index:
                ans += rev[idx:min_index]
                min_index = min(min_index, idx)
        
        return ans
            

s = Solution()
print(s.robotWithString("bac"))









    
        