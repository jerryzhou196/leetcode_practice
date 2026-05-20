class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        seen = {}
        candidates = sorted(candidates)

        def dfs(curr = [], total=0, index=0):
            nonlocal ans
            # print(curr, total, index)
            if total > target: 
                return False 
            
            if total == target: 
                ans.append(curr[:])
                return False
            
            for i, num in enumerate(candidates[index:]): 
                curr.append(num)
                res = dfs(curr, total + num, i + index)
                curr.pop()
                if not res: break

            return True

        dfs()
        return ans


# [2]
# [2 2]
# [2 2 2]
# [2 2 2 2]
# [2 2 3]

            


        