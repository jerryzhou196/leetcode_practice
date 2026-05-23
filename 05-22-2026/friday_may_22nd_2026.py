class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        def backtrack(y, curr = n, col=set(), antidiag=set(), diag=set()):
            if y == n:
                if curr == 0: 
                    ans.append(["".join(val) for val in board])
                return 
            
            diff = 0

            for x in range(n): 
                if x in col or y + x in diag or x - y in antidiag:
                    continue
                    
                diff = 1
                board[y][x] = 'Q'
                col.add(x)
                diag.add(y + x)
                antidiag.add(x - y)

                backtrack(y + 1, curr - diff, col, antidiag, diag)
            
                if diff: 
                    diff = 0
                    board[y][x] = '.'
                    col.remove(x)
                    diag.remove(y + x)
                    antidiag.remove(x - y)
        
        backtrack(0)
        return ans

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or val > self.min_heap[0]:
            heappush(self.min_heap, val)
            if len(self.min_heap) > self.k:
                heappop(self.min_heap)
        return self.min_heap[0]
                

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones: 
            heappush(heap, -1 * stone)
        
        while len(heap) >= 2: 
            rock1 = heappop(heap)
            rock2 = heappop(heap)

            heappush(heap, -1 * abs(rock2 - rock1))
        
        return -1 * heap[0]
        
        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def computeDistance(y1, x1, y2=0, x2=0):
            return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        heap = []
        
        for y, x in points:
            heappush(heap, (computeDistance(y, x), [y, x]))
        
        ans = []
        for i in range(k):
            _, point = heappop(heap)
            ans.append(point)
    
        return ans
        
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(nums, k):
            left, right, mid = [], [], []
            for num in nums:
                if num < nums[0]:
                    left.append(num)
                elif num > nums[0]: 
                    right.append(num)
                else:
                    mid.append(num)
            
            # print(left, mid, right, nums[0])
            
            if len(right) < k <= len(right) + len(mid): 
                return nums[0]
            elif k > len(right): 
                return quickSelect(left, k - len(mid) - len(right))
            else:
                return quickSelect(right, k)


        return quickSelect(nums, k)
        #     # [1,2,3,3,4]
        #     [1,2], [3,3] [4]
                

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        c = Counter(tasks)
        for item, count in c.items():
            heappush(heap, (count, item))

        curr = 0
        filled = 

        while heap:
            count, item = heappop(heap)
            curr += 1



