class Solution:
    def isInWindow(self, window, target_window):
        for char in target_window.keys():
            if window[char] < target_window[char]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        target_window = Counter(t)
        window_count = Counter()
        ans = [0, float('inf')]

        left =  0
        for r in range(len(s)):
            window_count[s[r]] += 1
            # print(r, window_count, target_window)
            while left <= r and self.isInWindow(window_count, target_window):
                # print(f"match: {left} - {r}", window_count, target_window)
                if r - left < ans[1] - ans[0]:
                    ans[0], ans[1] = left, r
                window_count[s[left]] -= 1
                left += 1
        
        return s[ans[0]:ans[1] + 1] if ans[1] < float('inf') else ""
