class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        Sum, ans = 0, 0
        cache = {}
        for i, n in enumerate(hours):
            Sum = Sum + 1 if n > 8 else Sum - 1
            if Sum > 0: ans = i + 1
            if Sum-1 in cache:
                ans = max(ans, i - cache[Sum-1])
            cache.setdefault(Sum, i)
        return ans