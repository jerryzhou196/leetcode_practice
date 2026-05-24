class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        heap = []
        for k, v in c.items(): 
            heappush(heap, [-v, k])

        ans = ""
        while heap: 
            v, k = heappop(heap)
            # print(heap, v, k)
            if not ans or ans[-1] != k: 
                ans += k
                if v < -1:
                    heappush(heap, [v + 1, k])
            else:
                if not heap: return ""
                next_v, next_k = heappop(heap)
                ans += next_k 
                if next_v < -1:
                    heappush(heap, [next_v + 1, next_k])
                heappush(heap, [v, k])

        return ans 

