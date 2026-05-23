from heapq import heappush, heappop
from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        c = Counter(tasks)
        for k, v in c.items():
            heappush(heap, -v)

        other = []
        time = 0
        while heap: 
            other.append(heappop(heap) + 1)
            tasks = 0
            print(heap, other, time)
            while heap and tasks < n + 1:
                other.append(heap.pop() + 1)
                tasks += 1
            
            for num in other: 
                if num < 0:
                    heappush(heap, num)

            other = []
            time += tasks if len(heap) == 0 else n + 1 

        return time 

s = Solution()
s.leastInterval(["A","A","A","B","B","B", "C","C","C", "D", "D", "E"], 2)

# A B C A B C A B C D E _ D


# ['A', 'B', 'C', 'A']
                

                





                

                
            




            
            
            
            


            

            
        
        # return ans

# A -> B -> C -> A -> B -> C -> A -> B -> C -> D -> E -> () -> D
# A -> B -> C -> D -> E -> A -> B -> C -> A -> B -> C -> D -> A 

# D -> E -> A -> D -> B -> A -> C -> B -> C -> A -> B -> C 

#         return ans

# ["B","C","D","A","A","A","A","G"]
# []
# (1,B), (2, C), (3, D), (4, A), (6, A), (8, A), (10, A), (5, G)

# (1, G) (2, A), (4, A), (6, A), (8, A)
# # (1,B), (2, C), (3, D), (4, A), (4, A), (4, A)


# B -> C -> D -> A -> G -> A -> idle -> A 
            
        
# #  ["A","A","A","B","B","B"], n = 2


# # offset = {
# #     A: 3 
# #     B: 1
# # }
# # next_available: 2
# # (1, A), (4, )






  

