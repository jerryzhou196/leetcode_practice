from heapq import heappush, heappop

class Solution:
    def getMinQueries(self, nums, queries): 
        operations = 0
        future_delta_array = [0] * (len(nums) + 1)
        queries.sort(key=lambda x: x[0])
        queries_we_ve_passed = []
        j = 0
        
        for i, num in enumerate(nums):
            operations += future_delta_array[i]
            while j < len(queries) and queries[j][0] == i: 
                heappush(queries_we_ve_passed, -queries[j][1])
                j += 1

            while operations < num and queries_we_ve_passed and -queries_we_ve_passed[0] >= i: 
                operations += 1
                future_delta_array[-heappop(queries_we_ve_passed) + 1] -= 1

            if operations < num: return -1 
                
        return len(queries_we_ve_passed)


nums = [2,0,2,3,3,2,1]
queries = [[0,2],[0,2],[1,1],[2,2], [1,2], [3,6], [3,6], [3,6]]
s = Solution()
print(s.getMinQueries(nums, queries))
                

