class HitCounter:
    def __init__(self):
        self.arr = []

    def hit(self, timestamp: int) -> None:
        self.arr.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        left, right = 0, len(self.arr) - 1
        search = max(timestamp - 300, 0)

        while left <= right:
            m = (left + right) // 2
            if self.arr[m] <= search:
                left = m + 1
            else:
                right = m - 1

        return len(self.arr) - left


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
